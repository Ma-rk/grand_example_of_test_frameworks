# Created by user at 2018-07-23
Feature: tests FileInfoContainer and FileInfoCollection
  # FileInfoContainer 와 FileInfoCollection 를 테스트함.

  Scenario: D:\Download\installed\calc.py 의 라인/메소드/클래스의 개수를 셈
    Given 읽어온 파일 내용
    When 읽어온 content 로 FileInfoContainer 객체를 생성하면
    Then line: 26 method: 4 class: 2

  Scenario: D:\Download\installed\에서 *.py 의 라인/메소드/클래스의 개수를 셈
    Given 읽어온 폴더 내용
    When 읽어온 content_list 로 FileInfoCollection 객체를 생성하면
    Then 2, 26, 4, 0, 7, 0, 1, 10, 1

  Scenario: 모킹한 데이터의 라인/메소드/클래스의 개수를 셈 for file
    Given generate_container_list 를 모킹 for file
    When 모킹한 데이터로 FileInfoCollection 객체를 생성하면 for file
    Then 2, 26, 4, 0, 7, 0, 1, 10, 1

  Scenario: 모킹한 데이터의 라인/메소드/클래스의 개수를 셈 for db
    Given generate_container_list 를 모킹 for db
    When 모킹한 데이터로 FileInfoCollection 객체를 생성하면 for db
    Then 2, 26, 4, 0, 7, 0, 1, 10, 1
