# gerador_curriculo.py
import os
from datetime import datetime

def gerar_curriculo():
    # Dados do currículo (fácil de editar)
    dados = {
        'nome': 'Pedro Augusto de Oliveira Lopes',
        'idade': 20,
        'telefone': '(62) 99826-2785',
        'email': 'pedrolopesvg007@gmail.com',
        'cidade': 'Itaberaí - GO',
        'sobre': '''Olá! Sou Pedro, tenho 20 anos e curso o 7º período de Sistemas de Informação na UEG. 
                   Tenho conhecimentos básicos em linguagens de programação, hardware e banco de dados. 
                   Possuo perfil proativo, autodidata e facilidade para trabalhar em equipe e aprender novas tecnologias.''',
        
        'formacao': {
            'curso': 'Sistemas de Informação',
            'instituicao': 'Universidade Estadual de Goiás',
            'periodo': 'Desde 2022',
            'status': '7º Período - Em andamento'
        },
        
        'experiencia': [
            {
                'empresa': 'Topagri',
                'cargo': 'Área de Topografia Técnica',
                'periodo': '2022-2025',
                'descricao': 'Atuação com AutoCAD para leitura e edição de plantas técnicas. Vivência prática com organização, medição e atenção a detalhes técnicos.'
            }
        ],
        
        'habilidades': {
            'programacao': ['Python(básico)', 'Java(básico)', 'PHP (básico)'],
            'tecnicas': ['Banco de dados (básico)', 'Manutenção de Hardware', 'Instalação de Softwares'],
            'ferramentas': ['AutoCAD', 'VS Code', 'Windows'],
            'idiomas': ['Inglês (básico)']
        },
        
        'cursos': [
            {
                'nome': 'Curso de Python – Básico ao Avançado',
                'status': 'Em andamento',
                'descricao': 'Atualmente aprofundando conhecimentos em Python, com foco em aplicações práticas.'
            }
        ]
    }
    
    # Template HTML com design moderno
    html_template = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{dados['nome']} - Currículo</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-color: #6366f1;
            --secondary-color: #8b5cf6;
            --accent-color: #06b6d4;
            --dark-color: #1e293b;
            --gray-color: #64748b;
            --light-gray: #f1f5f9;
            --white: #ffffff;
            --shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            --gradient: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 50%, var(--accent-color) 100%);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            line-height: 1.6;
            color: var(--dark-color);
            background: var(--gradient);
            min-height: 100vh;
            padding: 20px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: var(--white);
            border-radius: 24px;
            box-shadow: var(--shadow);
            overflow: hidden;
            display: grid;
            grid-template-columns: 380px 1fr;
            min-height: 90vh;
            position: relative;
        }}

        .container::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 6px;
            background: var(--gradient);
        }}

        /* SIDEBAR */
        .sidebar {{
            background: linear-gradient(145deg, #1e293b 0%, #334155 100%);
            color: var(--white);
            padding: 40px 30px;
            position: relative;
            overflow: hidden;
        }}

        .sidebar::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 50%);
            animation: float 6s ease-in-out infinite;
        }}

        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(180deg); }}
        }}

        .profile {{
            text-align: center;
            margin-bottom: 40px;
            position: relative;
            z-index: 2;
        }}

        .avatar {{
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: var(--gradient);
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            color: var(--white);
            box-shadow: 0 15px 35px rgba(0,0,0,0.3);
            position: relative;
            overflow: hidden;
        }}

        .avatar::before {{
            content: '';
            position: absolute;
            inset: 0;
            border-radius: 50%;
            padding: 3px;
            background: var(--gradient);
            mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            mask-composite: exclude;
        }}

        .profile h1 {{
            font-size: 26px;
            font-weight: 600;
            margin-bottom: 8px;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .profile .subtitle {{
            font-size: 14px;
            color: #94a3b8;
            font-weight: 300;
        }}

        .section {{
            margin-bottom: 35px;
            position: relative;
            z-index: 2;
        }}

        .section h2 {{
            font-size: 16px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-bottom: 20px;
            color: var(--white);
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .section h2::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: linear-gradient(90deg, var(--accent-color), transparent);
        }}

        .contact-item {{
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            padding: 12px;
            background: rgba(255,255,255,0.08);
            border-radius: 12px;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }}

        .contact-item:hover {{
            background: rgba(255,255,255,0.15);
            transform: translateX(8px);
        }}

        .contact-item i {{
            width: 20px;
            margin-right: 15px;
            color: var(--accent-color);
            font-size: 16px;
        }}

        .contact-item span {{
            font-size: 14px;
            font-weight: 400;
        }}

        .skill-category {{
            margin-bottom: 20px;
        }}

        .skill-category h3 {{
            font-size: 12px;
            color: #94a3b8;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 500;
        }}

        .skill-item {{
            background: rgba(255,255,255,0.1);
            padding: 8px 16px;
            margin: 8px 0;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 400;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.1);
        }}

        .skill-item:hover {{
            background: rgba(255,255,255,0.2);
            transform: scale(1.05);
            border-color: var(--accent-color);
        }}

        /* MAIN CONTENT */
        .main-content {{
            padding: 50px;
            background: var(--white);
        }}

        .main-header {{
            margin-bottom: 50px;
        }}

        .main-header h1 {{
            font-size: 48px;
            font-weight: 700;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 15px;
            line-height: 1.2;
        }}

        .main-header .tagline {{
            font-size: 20px;
            color: var(--gray-color);
            font-weight: 300;
        }}

        .main-section {{
            margin-bottom: 50px;
            position: relative;
        }}

        .main-section h2 {{
            font-size: 28px;
            font-weight: 600;
            color: var(--dark-color);
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            gap: 15px;
        }}

        .main-section h2 i {{
            color: var(--primary-color);
            font-size: 24px;
        }}

        .main-section h2::after {{
            content: '';
            flex: 1;
            height: 2px;
            background: linear-gradient(90deg, var(--primary-color), transparent);
            border-radius: 1px;
        }}

        .sobre-card {{
            background: var(--light-gray);
            padding: 30px;
            border-radius: 16px;
            border-left: 4px solid var(--primary-color);
            position: relative;
            overflow: hidden;
        }}

        .sobre-card::before {{
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 100px;
            height: 100px;
            background: radial-gradient(circle, var(--accent-color)20, transparent);
            border-radius: 50%;
        }}

        .sobre-text {{
            font-size: 16px;
            line-height: 1.8;
            color: var(--gray-color);
            text-align: justify;
            position: relative;
            z-index: 1;
        }}

        .item-card {{
            background: var(--white);
            padding: 25px;
            margin-bottom: 20px;
            border-radius: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border: 1px solid #e2e8f0;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }}

        .item-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: var(--gradient);
        }}

        .item-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            border-color: var(--primary-color);
        }}

        .item-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 15px;
        }}

        .item-title {{
            font-size: 20px;
            font-weight: 600;
            color: var(--dark-color);
            margin-bottom: 5px;
        }}

        .item-subtitle {{
            font-size: 16px;
            color: var(--primary-color);
            font-weight: 500;
        }}

        .item-period {{
            background: var(--gradient);
            color: var(--white);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            white-space: nowrap;
        }}

        .item-description {{
            color: var(--gray-color);
            font-size: 15px;
            line-height: 1.6;
        }}

        .formacao-card {{
            background: var(--light-gray);
            padding: 25px;
            border-radius: 16px;
            border-left: 4px solid var(--secondary-color);
        }}

        .formacao-title {{
            font-size: 22px;
            font-weight: 600;
            color: var(--dark-color);
            margin-bottom: 8px;
        }}

        .formacao-instituicao {{
            font-size: 18px;
            color: var(--secondary-color);
            font-weight: 500;
            margin-bottom: 8px;
        }}

        .formacao-detalhes {{
            display: flex;
            gap: 20px;
            align-items: center;
            margin-top: 15px;
        }}

        .formacao-periodo, .formacao-status {{
            background: var(--white);
            padding: 8px 16px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 500;
            color: var(--gray-color);
        }}

        /* RESPONSIVO */
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            
            .container {{
                grid-template-columns: 1fr;
                border-radius: 16px;
            }}
            
            .sidebar {{
                padding: 30px 20px;
            }}
            
            .main-content {{
                padding: 30px 20px;
            }}
            
            .main-header h1 {{
                font-size: 36px;
            }}
            
            .main-header .tagline {{
                font-size: 18px;
            }}
            
            .item-header {{
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
            }}
            
            .formacao-detalhes {{
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
            }}
        }}

        /* ANIMAÇÕES */
        .fade-in {{
            opacity: 0;
            transform: translateY(30px);
            animation: fadeInUp 0.8s ease forwards;
        }}

        @keyframes fadeInUp {{
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        .main-section:nth-child(1) {{ animation-delay: 0.1s; }}
        .main-section:nth-child(2) {{ animation-delay: 0.2s; }}
        .main-section:nth-child(3) {{ animation-delay: 0.3s; }}
        .main-section:nth-child(4) {{ animation-delay: 0.4s; }}
    </style>
</head>
<body>
    <div class="container">
        <!-- SIDEBAR -->
        <div class="sidebar">
            <div class="profile">
                <div class="avatar">
                    <i class="fas fa-user"></i>
                </div>
                <h1>{dados['nome']}</h1>
                <div class="subtitle">Desenvolvedor em Formação</div>
            </div>

            <div class="section">
                <h2><i class="fas fa-address-card"></i>Contato</h2>
                <div class="contact-item">
                    <i class="fas fa-phone"></i>
                    <span>{dados['telefone']}</span>
                </div>
                <div class="contact-item">
                    <i class="fas fa-envelope"></i>
                    <span>{dados['email']}</span>
                </div>
                <div class="contact-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <span>{dados['cidade']}</span>
                </div>
            </div>

            <div class="section">
                <h2><i class="fas fa-code"></i>Habilidades</h2>
                
                <div class="skill-category">
                    <h3>Programação</h3>
                    {gerar_skills(dados['habilidades']['programacao'])}
                </div>
                
                <div class="skill-category">
                    <h3>Técnicas</h3>
                    {gerar_skills(dados['habilidades']['tecnicas'])}
                </div>
                
                <div class="skill-category">
                    <h3>Ferramentas</h3>
                    {gerar_skills(dados['habilidades']['ferramentas'])}
                </div>
                
                <div class="skill-category">
                    <h3>Idiomas</h3>
                    {gerar_skills(dados['habilidades']['idiomas'])}
                </div>
            </div>
        </div>

        <!-- CONTEÚDO PRINCIPAL -->
        <div class="main-content">
            <div class="main-header">
                <h1>Pedro Augusto</h1>
                <div class="tagline">Sistemas de Informação • UEG</div>
            </div>

            <div class="main-section fade-in">
                <h2><i class="fas fa-user-circle"></i>Sobre Mim</h2>
                <div class="sobre-card">
                    <div class="sobre-text">
                        {dados['sobre'].strip()}
                    </div>
                </div>
            </div>

            <div class="main-section fade-in">
                <h2><i class="fas fa-graduation-cap"></i>Formação</h2>
                <div class="formacao-card">
                    <div class="formacao-title">{dados['formacao']['curso']}</div>
                    <div class="formacao-instituicao">{dados['formacao']['instituicao']}</div>
                    <div class="formacao-detalhes">
                        <div class="formacao-periodo">{dados['formacao']['periodo']}</div>
                        <div class="formacao-status">{dados['formacao']['status']}</div>
                    </div>
                </div>
            </div>

            <div class="main-section fade-in">
                <h2><i class="fas fa-briefcase"></i>Experiência</h2>
                {gerar_experiencias(dados['experiencia'])}
            </div>

            <div class="main-section fade-in">
                <h2><i class="fas fa-certificate"></i>Cursos Complementares</h2>
                {gerar_cursos(dados['cursos'])}
            </div>
        </div>
    </div>

    <script>
        // Adiciona animações quando a página carrega
        document.addEventListener('DOMContentLoaded', function() {{
            const elements = document.querySelectorAll('.fade-in');
            elements.forEach((el, index) => {{
                el.style.animationDelay = `${{index * 0.2}}s`;
            }});
        }});
    </script>
</body>
</html>'''

    return html_template

def gerar_skills(skills_list):
    """Gera HTML para lista de habilidades"""
    return '\n'.join([f'<div class="skill-item">{skill}</div>' for skill in skills_list])

def gerar_experiencias(experiencias):
    """Gera HTML para experiências"""
    html = ""
    for exp in experiencias:
        html += f'''
        <div class="item-card">
            <div class="item-header">
                <div>
                    <div class="item-title">{exp['empresa']}</div>
                    <div class="item-subtitle">{exp['cargo']}</div>
                </div>
                <div class="item-period">{exp['periodo']}</div>
            </div>
            <div class="item-description">{exp['descricao']}</div>
        </div>
        '''
    return html

def gerar_cursos(cursos):
    """Gera HTML para cursos"""
    html = ""
    for curso in cursos:
        html += f'''
        <div class="item-card">
            <div class="item-header">
                <div>
                    <div class="item-title">{curso['nome']}</div>
                </div>
                <div class="item-period">{curso['status']}</div>
            </div>
            <div class="item-description">{curso['descricao']}</div>
        </div>
        '''
    return html

def main():
    """Função principal"""
    print("🚀 Gerando seu currículo...")
    
    # Gera o HTML
    html_content = gerar_curriculo()
    
    # Salva o arquivo
    nome_arquivo = "curriculo_pedro.html"
    with open(nome_arquivo, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f"✅ Currículo gerado com sucesso!")
    print(f"📄 Arquivo: {nome_arquivo}")
    print(f"🌐 Abra o arquivo no navegador para visualizar")
    
    # Tenta abrir automaticamente no navegador
    try:
        import webbrowser
        webbrowser.open(f'file://{os.path.abspath(nome_arquivo)}')
        print("🔗 Abrindo no navegador...")
    except:
        print("💡 Abra manualmente o arquivo no seu navegador")

if __name__ == "__main__":
    main()