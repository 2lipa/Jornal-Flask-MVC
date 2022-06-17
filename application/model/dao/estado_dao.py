from application.model.entity import estado
from application.model.entity.estado import Estado

class EstadoDao:
    def __init__(self):
        self.estado = [
            Estado(0, 'Acre', 'AC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Acre-300x210.png'),
            Estado(1, 'Alagoas', 'AL', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Alagoas-300x200.png'),
            Estado(2, 'Amapá', 'AP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amapa-300x210.png' ),
            Estado(3, 'Amazonas', 'AM', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Amazonas-300x214.png' ),
            Estado(4, 'Bahia', 'BA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Bahia-300x200.png'),
            Estado(5, 'Ceará', 'CE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Ceara-300x210.png'),
            Estado(6, 'Distrito Federal', 'DF', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Distrito_Federal_Brasil-300x210.png'),
            Estado(7, 'Espírito Santo', 'ES', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Espirito_Santo-300x210.png'),
            Estado(8, 'Goiás', 'GO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Goias-300x210.png'),
            Estado(9, 'Maranhão', 'MA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Maranhao-300x200.png'),
            Estado(10, 'Mato Grosso', 'MT', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso-300x210.png'),
            Estado(11, 'Mato Grosso do Sul', 'MS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Mato_Grosso_do_Sul-300x210.png'),
            Estado(12, 'Minas Gerais', 'MG','https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Minas_Gerais-300x210.png'),
            Estado(13, 'Pará', 'PA', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Para-300x200.png'),
            Estado(14, 'Paraíba', 'PB', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_da_Paraiba-300x210.png'),
            Estado(15, 'Paraná', 'PR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Parana-300x210.png'),
            Estado(16, 'Pernambuco', 'PE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Pernambuco-300x210.png'),
            Estado(17, 'Piauí', 'PI', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Piaui-300x200.png'),
            Estado(18, 'Rio de Janeiro', 'RJ', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Rio_de_Janeiro-300x210.png'),
            Estado(19, 'Rio Grande do Norte', 'RN', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Norte-300x200.png'),
            Estado(20, 'Rio Grande do Sul', 'RS', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Rio_Grande_do_Sul-300x210.png'),
            Estado(21, 'Rondônia', 'RO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Rondonia-300x210.png'),
            Estado(22, 'Roraima', 'RR', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Roraima-300x200.png'),
            Estado(23, 'Santa Catarina', 'SC', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Santa_Catarina-300x218.png'),
            Estado(24, 'São Paulo', 'SP', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_Sao_Paulo-300x200.png'),
            Estado(25, 'Sergipe', 'SE', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_de_Sergipe-300x210.png'),
            Estado(26, 'Tocantins', 'TO', 'https://mundodageografia.com.br/wp-content/uploads/2020/10/Bandeira_do_Tocantins-300x210.png')
        ]
        

    def listar_estado(self):
        return self.estado

    def listar_estado_id(self, id):
        return self.estado[int(id)]