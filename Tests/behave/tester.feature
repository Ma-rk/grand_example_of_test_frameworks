# Created by Marc at 2018-07-19
Feature: tests Executor
  # Executor 를 테스트함.

  Scenario: 커맨드라인 인수 전달 pass command line argument
    Given argument is "D Download installed" 인수는 "D Download installed"
    When pass "D Download installed"
    Then executor.dir_path is "D Download installed"


  Scenario: 파일목록 작성하기
    Given Executor 객체, 파일 목록 instance of Executor, list of files
    When 파일목록 조회 read the list of files
    Then 주어진 목록과 조회한 목록이 일치 both of given list and actual list are equal


  Scenario: 파일목록에서 .py가 아닌 항목 제거하기
    Given 1. 파일목록, 2. .py가 아닌 항목 제거한 목록
    When 파일목록에서 .py가 아닌 항목을 제거했을 때
    Then 작업한 목록과 주어진 목록이 일치

