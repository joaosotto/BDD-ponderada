Feature: Acessibilidade e confiabilidade dos logs e dashboards
  Como um analista do time local
  Quero acessar logs e dashboards confiáveis
  Para revisar rapidamente as informações do sistema

  Scenario: O time acessa os logs corretamente
    Given existem logs disponíveis no sistema
    When o analista acessa o painel de logs
    Then ele deve visualizar os logs recentes com informações corretas
