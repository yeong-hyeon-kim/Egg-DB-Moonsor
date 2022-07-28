## 📕 프로젝트 개요(Introduce Project)
### 🍳 Egg(R)-DB Moonsor

* 관계형 데이터베이스를 조회하여 테이블 기술서를 작성합니다.

## 🏷️ 기능(Function)


* [Markdown, Html 형식의 테이블 기술서를 작성](#Markdown,-Html-형식의-테이블-기술서를-작성)


### 세부 기능(Function Detail)


#### Markdown, Html 형식의 테이블 기술서를 작성

   * 테이블과 컬럼을 조회하여 Markdown, Html 문법으로 테이블 기술서를 작성합니다.

## 💡 사용법(Tip)

 1. [config.json 데이터베이스 정보를 기입합니다.](/Egg-DB-Docs/config.json)
    * "EXPORT-EXTENSION": "출력할 확장자명을 기입합니다.
      * `MARKDOWN` OR `HTML`
    * "DBMS": "대상 DBMS를 기입합니다."
      * `SQL-SERVER`, `MY-SQL`, `MARIA-DB`, `ORACLE`
    * "SERVER": "`IP` 또는 `DOMAIN`을 기입합니다."
    * "USER": "사용자명을 기입합니다."
    * "PASSWORD" : "비밀번호를 기입합니다."
    * "DATABASE": "데이터베이스를 기입합니다."
 2. [SCRIPT.py 파일을 실행합니다.](/Egg-DB-Docs/SCRIPT.py)
 3. [SCRIPT.md 파일을 확인합니다.](/Egg-DB-Docs/SCRIPT.md) 또는 [SCRIPT.html 파일을 확인합니다.](/Egg-DB-Docs/SCRIPT.html)


## 💻 개발 환경(Develop Environment)


### 세부 환경(Environment Detail)

* ✔ OS : ![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=Windows&logoColor=white)
  * 🕒 Version : `10 Pro 21H2`
* ✔ Language : ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
  * 🕒 Version : `3.10.4`
* ✔ Dependency : [`requirements`](/Egg-DB-Docs/requirements.txt)


## 📖 비고(Remark)

* [Example Document](./ExDoc/SCRIPT.md)
