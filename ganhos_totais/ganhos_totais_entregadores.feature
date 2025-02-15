Feature: Validação da Exibição e Consistência dos Ganhos dos Entregadores

  Scenario Outline: Verificação da exibição e consistência dos ganhos
    Given que a API de ganhos está demorando para responder
    When a UI tenta recuperar os ganhos do entregador "<entregador>"
    Then os ganhos não devem ser exibidos na UI

    Given que um entregador possui um valor de ganho "<ganho_bruto>"
    When o backend realiza o arredondamento
    And a UI exibe o valor arredondado
    Then os valores devem ser idênticos

    Given que a UI está exibindo os ganhos do entregador "<entregador>"
    When eu realizo o cálculo esperado dos ganhos
    And eu consulto o valor exibido pela UI
    Then a diferença entre o valor calculado e o valor exibido deve ser menor que 0.5%

    Given que um entregador possui ganhos calculados
    When os ganhos são armazenados no banco de dados
    Then os valores recuperados do banco devem ser idênticos aos valores calculados

  Examples:
    | entregador | ganho_bruto | ganhosEsperados |
    | João       | 199.995     | 1500.00         |
    | Maria      | 150.235     | 2000.50         |
    | Pedro      | 49.875      | 1750.75         |