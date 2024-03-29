from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import IniciaInscricaoForm
from .forms import InscricaoEnccejaForm, InscricaoEnemForm, InscricaoHistoricoEscolarForm, InscricaoOutrosForm, InscricaoProvaoForm
from .models import Inscricao
from django.db.models import Q
from django.contrib.auth.models import User
from validate_docbr import CPF

# Create your views here.


@login_required
def continuar_inscricao(request):
    if (request.method == 'POST'):

        escolapublica = request.POST.get('escolapublica')
        pcd = request.POST.get('pcd')

        form = IniciaInscricaoForm(request.POST)

        return render(request, 'inscricao_seleciona.html', {
            'escolapublica': escolapublica,
            'pcd': pcd,
            'form': form,
        })


@login_required
def adicionar_inscricao(request):
    if (request.method == 'POST'):

        escolapublica = request.POST.get('escolapublica')
        rendainferior = request.POST.get('rendainferior')
        pcd = request.POST.get('pcd')
        ppi = request.POST.get('ppi')
        opcao = int(request.POST.get('opcao'))

        enquadramento = 'Ampla Concorrência'
        if pcd and not escolapublica and not rendainferior and not ppi:
            enquadramento = 'PcD'

        if escolapublica and rendainferior and ppi and pcd:
            enquadramento = 'RI-PPI-PcD'

        if escolapublica and rendainferior and ppi and not pcd:
            enquadramento = 'RI-PPI'

        if escolapublica and rendainferior and not ppi and pcd:
            enquadramento = 'RI-PcD'

        if escolapublica and rendainferior and not ppi and not pcd:
            enquadramento = 'RI-IE'

        if escolapublica and not rendainferior and ppi and pcd:
            enquadramento = 'RS-PPI-PcD'

        if escolapublica and not rendainferior and ppi and not pcd:
            enquadramento = 'RS-PPI'

        if escolapublica and not rendainferior and not ppi and pcd:
            enquadramento = 'RS-PcD'

        if escolapublica and not rendainferior and not ppi and not pcd:
            enquadramento = 'RS-IE'

        if opcao == 1:
            form = InscricaoHistoricoEscolarForm()
        if opcao == 2:
            form = InscricaoProvaoForm()
        if opcao == 3:
            form = InscricaoEnccejaForm()
        if opcao == 4:
            form = InscricaoEnemForm()
        if opcao == 5:
            form = InscricaoOutrosForm()

        if opcao == 0:
            form = IniciaInscricaoForm(request.POST)
            return render(request, 'inscricao_seleciona.html', {
                'escolapublica': escolapublica,
                'pcd': pcd,
                'form': form,
                'erro': 'Selecione uma opção de nota',
            })
        else:
            return render(request, 'inscricao_cont.html', {
                'opcao': opcao,
                'enquadramento': enquadramento,
                'form': form,
            })
    else:
        form = IniciaInscricaoForm()
        return render(request, 'inscricao.html', {'form': form})


@login_required
def salvar_inscricao(request):

    if (request.method == 'POST'):

        nomeresponsavel = request.POST.get('nomeresponsavel')
        cpfresponsavel = request.POST.get('cpfresponsavel')
        nomecandidato = request.POST.get('nomecandidato')
        cpfcandidato = request.POST.get('cpfcandidato')
        datanascimento = request.POST.get('datanascimento')
        endereco = request.POST.get('endereco')
        endereco_bairro = request.POST.get('endereco_bairro')
        endereco_cidade = request.POST.get('endereco_cidade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        docidentificacao = request.POST.get('docidentificacao')
        docidentificacao_emissor = request.POST.get('docidentificacao_emissor')
        nomepai = request.POST.get('nomepai')
        nomemae = request.POST.get('nomemae')
        opcaoinscricao = request.POST.get('opcaoinscricao'),

        opcao = int(request.POST.get('opcao'))
        if opcao == 1:
            form = InscricaoHistoricoEscolarForm(request.POST)
        if opcao == 2:
            form = InscricaoProvaoForm(request.POST)
        if opcao == 3:
            form = InscricaoEnccejaForm(request.POST)
        if opcao == 4:
            form = InscricaoEnemForm(request.POST)
        if opcao == 5:
            form = InscricaoOutrosForm(request.POST)

        consultacpf = Inscricao.objects.filter(cpfcandidato=cpfcandidato)

        if consultacpf.count() > 0:
            erro = "Já existe registro com esse nome, localize na lista e edite!"
        else:
            em_7_portugues = float(request.POST.get('em_7_portugues', 0))
            em_8_portugues = float(request.POST.get('em_8_portugues', 0))
            em_9_portugues = float(request.POST.get('em_9_portugues', 0))
            em_7_matematica = float(request.POST.get('em_7_matematica', 0))
            em_8_matematica = float(request.POST.get('em_8_matematica', 0))
            em_9_matematica = float(request.POST.get('em_9_matematica', 0))
            em_7_historia = float(request.POST.get('em_7_historia', 0))
            em_8_historia = float(request.POST.get('em_8_historia', 0))
            em_9_historia = float(request.POST.get('em_9_historia', 0))
            em_7_geografia = float(request.POST.get('em_7_geografia', 0))
            em_8_geografia = float(request.POST.get('em_8_geografia', 0))
            em_9_geografia = float(request.POST.get('em_9_geografia', 0))
            em_7_ciencias = float(request.POST.get('em_7_ciencias', 0))
            em_8_ciencias = float(request.POST.get('em_8_ciencias', 0))
            em_9_ciencias = float(request.POST.get('em_9_ciencias', 0))
            if (opcao == 1):
                mediaportugues = (em_7_portugues+em_8_portugues+em_9_portugues) / 3
                mediamatematica = (em_7_matematica+em_8_matematica+em_9_matematica) / 3
                mediahistoria = (em_7_historia+em_8_historia+em_9_historia) / 3
                mediageografia = (em_7_geografia+em_8_geografia+em_9_geografia) / 3
                mediaciencias = (em_7_ciencias+em_8_ciencias+em_9_ciencias) / 3
                media = (mediaportugues+mediamatematica+mediahistoria+mediageografia+mediaciencias) / 5

            provao_portugues = float(request.POST.get('provao_portugues', 0))
            provao_matematica = float(request.POST.get('provao_matematica', 0))
            provao_historia = float(request.POST.get('provao_historia', 0))
            provao_geografia = float(request.POST.get('provao_geografia', 0))
            provao_ciencias = float(request.POST.get('provao_ciencias', 0))
            if (opcao == 2):
                media = (provao_portugues+provao_matematica+provao_historia+provao_geografia+provao_ciencias) / 5

            encceja_portugues = float(request.POST.get('encceja_portugues', 0))
            encceja_matematica = float(request.POST.get('encceja_matematica', 0))
            encceja_historia = float(request.POST.get('encceja_historia', 0))
            encceja_geografia = float(request.POST.get('encceja_geografia', 0))
            encceja_ciencias = float(request.POST.get('encceja_ciencias', 0))
            mediaportugues = (encceja_portugues*100) / 180
            mediamatematica = (encceja_matematica*100) / 180
            mediahistoria = (encceja_historia*100) / 180
            mediageografia = (encceja_geografia*100) / 180
            mediaciencias = (encceja_ciencias*100) / 180
            if (opcao == 3):
                media = (mediaportugues+mediamatematica+mediahistoria+mediageografia+mediaciencias) / 5

            outros_portugues = float(request.POST.get('outros_portugues', 0))
            outros_matematica = float(request.POST.get('outros_matematica', 0))
            outros_historia = float(request.POST.get('outros_historia', 0))
            outros_geografia = float(request.POST.get('outros_geografia', 0))
            outros_ciencias = float(request.POST.get('outros_ciencias', 0))
            if (opcao == 5):
                media = (outros_portugues+outros_matematica+outros_historia+outros_geografia+outros_ciencias) / 5

            enem_linguagens = float(request.POST.get('enem_linguagens', 0))
            enem_matematica = float(request.POST.get('enem_matematica', 0))
            if (opcao == 4):
                media = ((enem_linguagens/10) + (enem_matematica/10)) / 2

            novoregistro = Inscricao(
                nomeresponsavel=request.POST.get('nomeresponsavel'),
                cpfresponsavel=request.POST.get('cpfresponsavel'),
                nomecandidato=request.POST.get('nomecandidato'),
                cpfcandidato=request.POST.get('cpfcandidato'),
                datanascimento=request.POST.get('datanascimento'),
                endereco=request.POST.get('endereco'),
                endereco_bairro=request.POST.get('endereco_bairro'),
                endereco_cidade=request.POST.get('endereco_cidade'),
                email=request.POST.get('email'),
                telefone=request.POST.get('telefone'),
                docidentificacao=request.POST.get('docidentificacao'),
                docidentificacao_emissor=request.POST.get('docidentificacao_emissor'),
                nomepai=request.POST.get('nomepai'),
                nomemae=request.POST.get('nomemae'),
                opcaoinscricao=request.POST.get('opcaoinscricao'),
                em_7_portugues=float(request.POST.get('em_7_portugues', 0)),
                em_8_portugues=float(request.POST.get('em_8_portugues', 0)),
                em_9_portugues=float(request.POST.get('em_9_portugues', 0)),
                em_7_matematica=float(request.POST.get('em_7_matematica', 0)),
                em_8_matematica=float(request.POST.get('em_8_matematica', 0)),
                em_9_matematica=float(request.POST.get('em_9_matematica', 0)),
                em_7_historia=float(request.POST.get('em_7_historia', 0)),
                em_8_historia=float(request.POST.get('em_8_historia', 0)),
                em_9_historia=float(request.POST.get('em_9_historia', 0)),
                em_7_geografia=float(request.POST.get('em_7_geografia', 0)),
                em_8_geografia=float(request.POST.get('em_8_geografia', 0)),
                em_9_geografia=float(request.POST.get('em_9_geografia', 0)),
                em_7_ciencias=float(request.POST.get('em_7_ciencias', 0)),
                em_8_ciencias=float(request.POST.get('em_8_ciencias', 0)),
                em_9_ciencias=float(request.POST.get('em_9_ciencias', 0)),
                provao_portugues=float(request.POST.get('provao_portugues', 0)),
                provao_matematica=float(request.POST.get('provao_matematica', 0)),
                provao_historia=float(request.POST.get('provao_historia', 0)),
                provao_geografia=float(request.POST.get('provao_geografia', 0)),
                provao_ciencias=float(request.POST.get('provao_ciencias', 0)),
                encceja_portugues=float(request.POST.get('encceja_portugues', 0)),
                encceja_matematica=float(request.POST.get('encceja_matematica', 0)),
                encceja_historia=float(request.POST.get('encceja_historia', 0)),
                encceja_geografia=float(request.POST.get('encceja_geografia', 0)),
                encceja_ciencias=float(request.POST.get('encceja_ciencias', 0)),
                outros_portugues=float(request.POST.get('outros_portugues', 0)),
                outros_matematica=float(request.POST.get('outros_matematica', 0)),
                outros_historia=float(request.POST.get('outros_historia', 0)),
                outros_geografia=float(request.POST.get('outros_geografia', 0)),
                outros_ciencias=float(request.POST.get('outros_ciencias', 0)),
                enem_linguagens=float(request.POST.get('enem_linguagens', 0)),
                enem_matematica=float(request.POST.get('enem_matematica', 0)),
                media=media,
                usuarioinseriu=request.user,
            )

            novoregistro.save()
            return redirect('inscricao:relatorio')

        return render(request, 'inscricao_cont.html', {
            'erro': erro,
            'form': form,
            'opcao': str(opcao),
            'enquadramento': opcaoinscricao[0],
        })
    else:
        return redirect('inscricao:inscricao')


@login_required
def ficha_inscricao(request, id):

    cpf = CPF()

    dados = get_object_or_404(Inscricao, pk=id)

    cpfcandidato = cpf.mask(str(dados.cpfcandidato))
    cpfresponsavel = cpf.mask(str(dados.cpfresponsavel))

    dados.cpfresponsavel = cpfresponsavel
    dados.cpfcandidato = cpfcandidato

    return render(request, 'ficha_inscricao.html', {
        'codinscricao': id,
        'dados': dados,
    })


def gerarpdf(request, id):
    dados = get_object_or_404(Inscricao, pk=id)

    from django.http import HttpResponse
    from django.template.loader import render_to_string
    from weasyprint import HTML

    html_string = render_to_string('ficha_inscricao.html', {'dados': dados, 'codinscricao': id})

    pdf_file = HTML(string=html_string).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="fichainscricao.pdf"'

    return response


@login_required
def relatorio_inscricao(request):

    termofiltro = request.POST.get('p_filtro', '')

    if termofiltro != '':
        filtro = (Q(nomecandidato__icontains=termofiltro))
        filtro.add(Q(cpfcandidato__icontains=termofiltro), Q.OR)
        lista_inscritos = Inscricao.objects.filter(filtro)
    else:
        lista_inscritos = Inscricao.objects.all()

    totalinscritos = lista_inscritos.count()
    paginator = Paginator(lista_inscritos, 100)
    page = request.GET.get('page', 1)
    lista_inscritos = paginator.get_page(page)

    return render(request, 'relatorio_inscricao.html', {
        'registros': lista_inscritos,
        'totalinscritos': totalinscritos,
    })

@login_required
def relatorio_inscricao_cotas(request):

    lista_inscritos = Inscricao.objects.all().order_by('opcaoinscricao', '-media')

    paginator = Paginator(lista_inscritos, 100)
    page = request.GET.get('page', 1)
    lista_inscritos = paginator.get_page(page)

    return render(request, 'relatorio_inscricao_cotas.html', {
        'registros': lista_inscritos,
    })

@login_required
def editar_inscricao(request, id):
    pass


@login_required
def apagar_inscricao(request, id):
    registro = get_object_or_404(Inscricao, pk=id)
    registro.delete()
    return redirect('inscricao:relatorio')
