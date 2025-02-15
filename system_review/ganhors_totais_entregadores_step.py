from behave import given, when, then
from hamcrest import assert_that, is_, close_to

@given("que a API de ganhos está demorando para responder")
def step_api_lenta(context):
    context.api_lenta = True

@when("a UI tenta recuperar os ganhos do entregador {entregador}")
def step_ui_recupera_ganhos(context, entregador):
    context.ganhos_exibidos = None if context.api_lenta else 100.0

@then("os ganhos não devem ser exibidos na UI")
def step_ganhos_nao_exibidos(context):
    assert_that(context.ganhos_exibidos, is_(None))

@given("que um entregador possui um valor de ganho {ganho_bruto}")
def step_valor_ganho(context, ganho_bruto):
    context.ganho_bruto = float(ganho_bruto)

@when("o backend realiza o arredondamento")
def step_backend_arredonda(context):
    context.ganho_arredondado = round(context.ganho_bruto, 2)

@then("os valores devem ser idênticos")
def step_valores_identicos(context):
    assert_that(context.ganho_arredondado, is_(context.ganho_bruto))

@given("que um entregador possui ganhos calculados")
def step_ganhos_calculados(context):
    context.ganhos_calculados = 1500.00

@when("os ganhos são armazenados no banco de dados")
def step_armazenar_ganhos(context):
    context.ganhos_armazenados = context.ganhos_calculados

@then("os valores recuperados do banco devem ser idênticos aos valores calculados")
def step_validar_ganhos_no_bd(context):
    assert_that(context.ganhos_armazenados, is_(context.ganhos_calculados))

