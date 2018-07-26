# Created by user at 2018-07-23
Feature: tests FileInfoContainer and FileInfoCollection
  # FileInfoContainer 와 FileInfoCollection 를 테스트함.

  Scenario: D:\Download\installed\calc.py 의 라인/메소드/클래스의 개수를 셈
    Given 읽어온 파일 내용
    When 읽어온 content 로 FileInfoContainer 객체를 생성하면
    Then line: 26 method: 4 class: 2
