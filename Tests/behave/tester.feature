# Created by user at 2018-07-23
Feature: tests FileInfoContainer and FileInfoCollection
  # FileInfoContainer 와 FileInfoCollection 를 테스트함.

  Scenario: D:\Download\installed\calc.py 의 라인/메소드/클래스의 개수를 셈
    Given 파일명 D Download installed calc.py
    When D Download installed calc.py 로 FileInfoContainer 객체를 생성하면
    Then line: 26 method: 4 class: 2


  Scenario: D:\Download\installed\의 *.py 의 라인/메소드/클래스의 개수를 셈
    Given 경로 D Download installed
    When D Download installed 로 FileInfoCollection 객체를 생성하면
    Then 26/4/2 7/0/0 10/1/1
