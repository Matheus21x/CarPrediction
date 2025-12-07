from main import df 
from ydata_profiling import ProfileReport 

profile = ProfileReport(df, title="Relatório de Preços de Carros", explorative=True)

print("Gerando relatório, aguarde...")
profile.to_file("relatorio_carros.html")
print("Relatório salvo com sucesso!")