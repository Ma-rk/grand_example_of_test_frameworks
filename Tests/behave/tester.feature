# Created by Marc at 2018-07-19
Feature: tests Executor
  # Executor 를 테스트함.

  Scenario: 커맨드라인 인수 전달 pass command line argument
    Given argument is "D Download installed" 인수는 "D Download installed"
    When pass "D Download installed"
    Then executor.dir_path is "D Download installed"
