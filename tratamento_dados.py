import pandas as pd

file = "arquivo_a_tratar_xlsx"

df = pd.read_excel(file)

filtrando_colunas = df[['Paciente', 'DtNascimento', 'E_Mail', 'Celular']]

df = filtrando_colunas

#nomes
df = df.drop_duplicates(subset='Paciente', keep='first')

#email
email_dropado = df[df['E_Mail'].isnull()]

df = df.dropna(subset=['E_Mail'])
df.loc[:, 'E_Mail'] = df['E_Mail'].str.lower()
df.loc[df['E_Mail'].str.contains(' ', na=False), 'E_Mail'] = None

#telefones
telefone_dropado = df[df['Celular'].isnull()]
df = df.dropna(subset=['Celular'])

df.loc[:, 'Celular'] = df['Celular'].astype(str)

ddd = 11
df.loc[:, 'Celular'] = str(ddd) + df['Celular']
df.loc[:, 'Celular'] = df['Celular'].str.replace('-', '')

#saida
saida = 'salvar_arquivo_tratado_xlsx'
df.to_excel(saida, index=False)

print(df.head())