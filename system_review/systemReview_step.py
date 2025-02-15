from behave import given, when, then
from hamcrest import assert_that, greater_than, is_, contains_string, all_of
from mocks.mock_system_review import get_system_logs

logs =[]

@given("existem logs disponíveis no sistema")
def step_given_logs_disponiveis(context):
global logs
logs = get_system_logs()
assert_that(len(logs), greater_than(0))

@when("o analista acessa o painel de logs")
def step_when_acessa_painel(context):
print("O analista acessou o painel de logs.")

@then("ele deve visualizar os logs recentes com informações corretas")
def step_then_verifica_logs(context):
assert_that(logs, is_(not None))
assert_that(logs, is_(not[]))
assert_that(logs[0], contains_string("INFO"))
assert_that(all(map(lambda log: isinstance(log, str), logs)), is_(True))