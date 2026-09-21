import os
import requests
import pandas as pd

# Mapeamento das ligas com ID da ESPN e nome da pasta de destino
LIGAS = {
    'Premier League': {
        'id': 'eng.1',
        'pasta': 'liga_inglesa'
    },
    'La Liga': {
        'id': 'esp.1',
        'pasta': 'la_liga'
    },
    'Brasileirão Série A': {
        'id': 'bra.1',
        'pasta': 'brasileirao'
    }
}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def extrair_e_salvar_liga(nome_liga: str, league_id: str, pasta_destino: str) -> pd.DataFrame | None:
    """Extrai a tabela da ESPN API, cria um DataFrame

    e salva em um arquivo CSV em cada pasta.
    """
    url = f'https://site.web.api.espn.com/apis/v2/sports/soccer/{league_id}/standings'
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"Erro ao acessar {nome_liga}: Status Code {response.status_code}")
        return None

    data = response.json()

    try:
        entradas = data['children'][0]['standings']['entries'] #estrutura do JSON da API da ESPN
        lista_times = []

        for entrada in entradas:
            stats = entrada.get('stats', [])

            def get_stat(stat_name):
                return next((s['value'] for s in stats if s.get('name') == stat_name), 0) # Função p/ trazer cadada estatistica por nome  uma unica vez e ordenar o valor, caso não exista retorna 0
            # Mapeando as colunas de interesse
            dados_time = {
                'posicao': int(get_stat('rank')),
                'time': entrada['team']['displayName'],
                'pontos': int(get_stat('points')),
                'jogos': int(get_stat('gamesPlayed')),
                'vitorias': int(get_stat('wins')),
                'empates': int(get_stat('ties')),
                'derrotas': int(get_stat('losses')),
                'gols_pro': int(get_stat('pointsFor')),
                'gols_contra': int(get_stat('pointsAgainst'))
            }
            lista_times.append(dados_time)

        # Criação do DataFrame do Pandas
        df = pd.DataFrame(lista_times)

        # Pastas de destino
        os.makedirs(pasta_destino, exist_ok=True)

        # Caminho do arquivo CSV
        caminho_csv = os.path.join(pasta_destino, 'tabela.csv')

        # Salva em CSV com suporte a caracteres especiais (Acentos e Ç)
        df.to_csv(caminho_csv, index=False, encoding='utf-8-sig')
        print(f"✅ {nome_liga}: Salvo com sucesso em '{caminho_csv}' ({len(df)} times)")

        return df

    except (KeyError, IndexError) as e:
        print(f"Erro ao processar a estrutura JSON da liga {nome_liga}: {e}")
        return None


# Execução do pipeline para todas as ligas
if __name__ == '__main__':
    dataframes = {}

    for nome_liga, config in LIGAS.items():
        df_liga = extrair_e_salvar_liga(
            nome_liga=nome_liga,
            league_id=config['id'],
            pasta_destino=config['pasta']
        )
        if df_liga is not None:
            dataframes[config['pasta']] = df_liga