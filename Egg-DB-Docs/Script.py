from dataclasses import replace
import datetime
import pymssql
import pymysql
import cx_Oracle
import json

# Config
server = ""
user = ""
password = ""
databases = ""
dbms = ""

# Output Final Markdown.
OutputString = ""


def ReadJson(Path, Mode):
    with open(Path, Mode) as f:
        json_data = json.load(f)
        return json_data


def WriteFile(Path, Mode, Data):
    with open(Path, Mode) as f:
        f.write(Data)
        f.close()


def ReturnQueryByDbms(dbms):
    QueryString = {}

    if dbms == "SQL-SERVER":
        QueryString["TABLE"] = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES ORDER BY TABLE_NAME"
        QueryString["COLUMN"] = "SELECT ORDINAL_POSITION, COLUMN_NAME, IS_NULLABLE, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "
    elif dbms == "MY-SQL" or dbms == "MARIA-DB":
        QueryString["TABLE"] = "SHOW TABLES"
        QueryString["COLUMN"] = "SHOW FULL COLUMNS FROM "
    elif dbms == "ORACLE":
        QueryString["TABLE"] = "SELECT * FROM USER_TABLES"
        QueryString["COLUMN"] = "SELECT * FROM COLS WHERE TABLE_NAME ="
    else:
        QueryString["TABLE"] = ""
        QueryString["COLUMN"] = ""

    return QueryString


def SetConfig():
    Datas = ReadJson('./Egg-DB-Docs/config.json', 'r')

    global server
    global user
    global password
    global databases
    global dbms

    server = str(Datas["CONNECTION"]["SERVER"])
    user = str(Datas["CONNECTION"]["USER"])
    password = str(Datas["CONNECTION"]["PASSWORD"])
    databases = str(Datas["CONNECTION"]["DATABASE"])
    dbms = str(Datas["DBMS"])


def GenDescriptionString(DataList, HeaderText, Type):
    try:

        if Type == "TABLE":
            DocString = "### " + HeaderText.replace("'", "") + "\n\n"
            DocString += "|TABLE_NAME|DESCRIPTION|" + "\n"
            DocString += "|:---------|:----------|" + "\n"

            for i in range(0, len(DataList)):
                DocString += "|[" + str(DataList[i][0]) + "](#" + \
                    str(DataList[i][0]).replace("'", "") + ")||\n"

        elif Type == "COLUMN":
            DocString = "#### " + HeaderText.replace("'", "") + "\n\n"
            DocString += "|ORDINAL_POSITION|COLUMN_NAME|IS_NULLABLE|DATA_TYPE|DESCRIPTION|" + "\n"
            DocString += "|:---------------|:----------|:---------:|:--------|:----------|" + "\n"

            print(DocString)

            # [0] ORDINAL_POSITION
            # [1] COLUMN_NAME
            # [2] IS_NULLABLE
            # [3] DATA_TYPE
            # [4] DESCRIPTION
            for i in range(0, len(DataList)):
                DocString += "|" + str(DataList[i][0]) + "|`" + str(DataList[i][1]) + "`|" + str(
                    DataList[i][2]) + "|" + str(DataList[i][3]) + "||\n"

        DocString += "\n"

        print(DocString)

        global OutputString
        OutputString += DocString
    except:
        pass


def GenSignature(Mode):
    global OutputString

    if Mode == "HEADER":
        Sign = "## Table Description \n"
        Sign += ">_Update Date : " + str(datetime.datetime.utcnow()) + "_\n"
    elif Mode == "FOOTER":
        Sign = ""

    OutputString += Sign


def SelectDbStructure(server, user, password, databases, dbms):
    try:
        # Connection By DBMS.
        if dbms == "SQL-SERVER":
            conn = pymssql.connect(
                server=server, user=user, password=password, database=databases
            )
        elif dbms == "MY-SQL" or dbms == "MARIA-DB":
            conn = pymysql.connect(
                server=server, user=user, password=password, database=databases
            )
        elif dbms == "ORACLE":
            conn = cx_Oracle.connect(
                server=server, user=user, password=password, database=databases
            )
        else:
            print()

        cursor = conn.cursor()

        # Request Query By DBMS.
        QueryString = ReturnQueryByDbms(dbms)

        print(QueryString["TABLE"])

        # Select Table List.
        cursor.execute(QueryString["TABLE"])
        row = cursor.fetchone()

        # Init List.
        LIST_TABLE = []
        LIST_TABLE_COLUMN = []

        print(len(row))

        while row:
            LIST_TABLE.append(row)
            row = cursor.fetchone()

        # --------------------------------

        print(len(LIST_TABLE))

        GenSignature("HEADER")

        TableList = LIST_TABLE

        GenDescriptionString(TableList, "Table List", "TABLE")

        for i in range(0, len(LIST_TABLE)):
            print(LIST_TABLE[i])

            TableName = str(LIST_TABLE[i])[1:-2]

            print(TableName)
            print(QueryString["COLUMN"] + TableName)

            # Select Columns By Table.
            cursor.execute(QueryString["COLUMN"] + TableName)
            rows = cursor.fetchone()

            while rows:
                LIST_TABLE_COLUMN.append(rows)
                rows = cursor.fetchone()

            # --------------------------------

            ColList = LIST_TABLE_COLUMN

            print(LIST_TABLE_COLUMN)

            GenDescriptionString(ColList, TableName, "COLUMN")

            # Next Table.
            LIST_TABLE_COLUMN.clear()

        conn.close()

        GenSignature("FOOTER")
        WriteFile("./Egg-DB-Docs/SCRIPT.md", "w", OutputString)
    except:
        pass


SetConfig()
SelectDbStructure(server, user, password, databases, dbms)
