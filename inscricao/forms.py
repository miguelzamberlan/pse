from django import forms
from django.forms import ModelForm
from .models import Inscricao


class InscricaoHistoricoEscolarForm(ModelForm):

    email = forms.CharField(
        required=False,
        label="E-mail",
        max_length=200,
    )

    class Meta:
        model = Inscricao

        fields = [
                'nomeresponsavel',
                'cpfresponsavel',
                'nomecandidato',
                'cpfcandidato',
                'datanascimento',
                'endereco',
                'endereco_bairro',
                'endereco_cidade',
                'email',
                'telefone',
                'docidentificacao',
                'docidentificacao_emissor',
                'nomepai',
                'nomemae',
                'em_7_portugues',
                'em_8_portugues',
                'em_9_portugues',
                'em_7_matematica',
                'em_8_matematica',
                'em_9_matematica',
                'em_7_historia',
                'em_8_historia',
                'em_9_historia',
                'em_7_geografia',
                'em_8_geografia',
                'em_9_geografia',
                'em_7_ciencias',
                'em_8_ciencias',
                'em_9_ciencias',
            ]

        #widgets = {'cpfcandidato': forms.TextInput(attrs={'data-mask': "000-000-0000"})}

        labels = {
            'nomeresponsavel': 'Nome do responsável pelo candidato',
            'cpfresponsavel': 'CPF do responsável pelo candidato',
            'nomecandidato': 'Nome do candidato',
            'cpfcandidato': 'CPF do candidato',
            'datanascimento': 'Data de Nascimento',
            'endereco': 'Endereço Completo',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'docidentificacao': 'Número do Documento de Indentificação',
            'docidentificacao_emissor': 'Tipo Documento Identificação',
            'nomepai': 'Nome do pai',
            'nomemae': 'Nome mãe',
            'em_7_portugues': 'Nota 7º Período de Português',
            'em_8_portugues': 'Nota 8º Período de Português',
            'em_9_portugues': 'Nota 9º Período de Português',
            'em_7_matematica': 'Nota 7º Período de Matemática',
            'em_8_matematica': 'Nota 8º Período de Matemática',
            'em_9_matematica': 'Nota 9º Período de Matemática',
            'em_7_historia': 'Nota 7º Período de História',
            'em_8_historia': 'Nota 8º Período de História',
            'em_9_historia': 'Nota 9º Período de História',
            'em_7_geografia': 'Nota 7º Período de Geografia',
            'em_8_geografia': 'Nota 8º Período de Geografia',
            'em_9_geografia': 'Nota 9º Período de Geografia',
            'em_7_ciencias': 'Nota 7º Período de Ciências',
            'em_8_ciencias': 'Nota 8º Período de Ciências',
            'em_9_ciencias': 'Nota 9º Período de Ciências',
        }

class InscricaoProvaoForm(ModelForm):

    class Meta:
        model = Inscricao

        fields = [
                'nomeresponsavel',
                'cpfresponsavel',
                'nomecandidato',
                'cpfcandidato',
                'datanascimento',
                'endereco',
                'endereco_bairro',
                'endereco_cidade',
                'email',
                'telefone',
                'docidentificacao',
                'docidentificacao_emissor',
                'nomepai',
                'nomemae',
                'provao_portugues',
                'provao_matematica',
                'provao_historia',
                'provao_geografia',
                'provao_ciencias',
            ]


        labels = {
            'nomeresponsavel': 'Nome do responsável pelo candidato',
            'cpfresponsavel': 'CPF do responsável pelo candidato',
            'nomecandidato': 'Nome do candidato',
            'cpfcandidato': 'CPF do candidato',
            'datanascimento': 'Data de Nascimento',
            'endereco': 'Endereço Completo',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'docidentificacao': 'Número do Documento de Indentificação',
            'docidentificacao_emissor': 'Tipo Documento Identificação',
            'nomepai': 'Nome do pai',
            'nomemae': 'Nome mãe',
            'provao_portugues': 'Nota Provão Português',
            'provao_matematica': 'Nota Provão Matemática',
            'provao_historia': 'Nota Provão História',
            'provao_geografia': 'Nota Provão Geografia',
            'provao_ciencias': 'Nota Provão Ciências',
        }

class InscricaoEnccejaForm(ModelForm):

    class Meta:
        model = Inscricao

        fields = [
                'nomeresponsavel',
                'cpfresponsavel',
                'nomecandidato',
                'cpfcandidato',
                'datanascimento',
                'endereco',
                'endereco_bairro',
                'endereco_cidade',
                'email',
                'telefone',
                'docidentificacao',
                'docidentificacao_emissor',
                'nomepai',
                'nomemae',
                'encceja_portugues',
                'encceja_matematica',
                'encceja_historia',
                'encceja_geografia',
                'encceja_ciencias',
            ]


        labels = {
            'nomeresponsavel': 'Nome do responsável pelo candidato',
            'cpfresponsavel': 'CPF do responsável pelo candidato',
            'nomecandidato': 'Nome do candidato',
            'cpfcandidato': 'CPF do candidato',
            'datanascimento': 'Data de Nascimento',
            'endereco': 'Endereço Completo',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'docidentificacao': 'Número do Documento de Indentificação',
            'docidentificacao_emissor': 'Tipo Documento Identificação',
            'nomepai': 'Nome do pai',
            'nomemae': 'Nome mãe',
            'encceja_portugues': 'Nota do ENCCEJA Português',
            'encceja_matematica': 'Nota do ENCCEJA Matemática',
            'encceja_historia': 'Nota do ENCCEJA História',
            'encceja_geografia' : 'Nota do ENCCEJA Geografia',
            'encceja_ciencias': 'Nota do ENCCEJA Ciências',
        }


class InscricaoEnemForm(ModelForm):

    class Meta:
        model = Inscricao

        fields = [
                'nomeresponsavel',
                'cpfresponsavel',
                'nomecandidato',
                'cpfcandidato',
                'datanascimento',
                'endereco',
                'endereco_bairro',
                'endereco_cidade',
                'email',
                'telefone',
                'docidentificacao',
                'docidentificacao_emissor',
                'nomepai',
                'nomemae',
                'enem_linguagens',
                'enem_matematica',
            ]


        labels = {
            'nomeresponsavel': 'Nome do responsável pelo candidato',
            'cpfresponsavel': 'CPF do responsável pelo candidato',
            'nomecandidato': 'Nome do candidato',
            'cpfcandidato': 'CPF do candidato',
            'datanascimento': 'Data de Nascimento',
            'endereco': 'Endereço Completo',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'docidentificacao': 'Número do Documento de Indentificação',
            'docidentificacao_emissor': 'Tipo Documento Identificação',
            'nomepai': 'Nome do pai',
            'nomemae': 'Nome mãe',
            'enem_linguagens': 'Nota do ENEM Linguagens, Códigos e suas Tecnologias',
            'enem_matematica': 'Nota do ENEM Matemática e suas Tecnologias',
        }

class InscricaoOutrosForm(ModelForm):

    class Meta:
        model = Inscricao

        fields = [
                'nomeresponsavel',
                'cpfresponsavel',
                'nomecandidato',
                'cpfcandidato',
                'datanascimento',
                'endereco',
                'endereco_bairro',
                'endereco_cidade',
                'email',
                'telefone',
                'docidentificacao',
                'docidentificacao_emissor',
                'nomepai',
                'nomemae',
                'outros_portugues',
                'outros_matematica',
                'outros_historia',
                'outros_geografia',
                'outros_ciencias'
            ]


        labels = {
            'nomeresponsavel': 'Nome do responsável pelo candidato',
            'cpfresponsavel': 'CPF do responsável pelo candidato',
            'nomecandidato': 'Nome do candidato',
            'cpfcandidato': 'CPF do candidato',
            'datanascimento': 'Data de Nascimento',
            'endereco': 'Endereço Completo',
            'endereco_bairro': 'Bairro',
            'endereco_cidade': 'Cidade',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'docidentificacao': 'Número do Documento de Indentificação',
            'docidentificacao_emissor': 'Tipo Documento Identificação',
            'nomepai': 'Nome do pai',
            'nomemae': 'Nome mãe',
            'outros_portugues': 'Outros casos - Português',
            'outros_matematica': 'Outros casos - Matemática',
            'outros_historia': 'Outros casos - História',
            'outros_geografia': 'Outros casos - Geografia',
            'outros_ciencias': 'Outros casos - Ciências',
        }


class IniciaInscricaoForm(forms.Form):
    escolapublica = forms.BooleanField(label='Estudou sempre em escola pública?', required=False)
    rendainferior = forms.BooleanField(label='Possuí renda familiar inferior a 1,5 salário?', required=False)
    pcd = forms.BooleanField(label='Pessoa com deficiência (PCD)?', required=False)
    ppi = forms.BooleanField(label='Se declara Preto, Pardo ou indígena?', required=False)
