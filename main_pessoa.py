from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica


pessoa = Pessoa("João", "123456", "2024-01-01", True)
print("Informações da Pessoa:")
pessoa.imprimir_informacoes()


pessoa_fisica = PessoaFisica("Maria", "654321", "2024-02-01", True, "1990-03-15", "123.456.789-01", "MG-1234567")
print("\nInformações da Pessoa Física:")
pessoa_fisica.imprimir_informacoes()


pessoa_juridica = PessoaJuridica("Empresa X", "789456", "2024-03-01", True, "2024-01-01", "12.345.678/0001-99")
print("\nInformações da Pessoa Jurídica:")
pessoa_juridica.imprimir_informacoes()


try:
    pessoa_fisica.cpf = "123.456.789-0"  
except ValueError as e:
    print(f"\nErro: {e}")

pessoa_fisica.cpf = "123.456.789-01" 

try:
    pessoa_juridica.cnpj = "12.345.678/0001-9" 
except ValueError as e:
    print(f"\nErro: {e}")

pessoa_juridica.cnpj = "12.345.678/0001-99" 


print("\nInformações da Pessoa Física após atualização:")
pessoa_fisica.imprimir_informacoes()

print("\nInformações da Pessoa Jurídica após atualização:")
pessoa_juridica.imprimir_informacoes()