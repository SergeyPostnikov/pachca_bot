import plotly.graph_objects as go

options = ['Опция 1', 'Опция 2']
votes = [150, 50]

fig = go.Figure(data=[go.Pie(labels=options, values=votes, hole=.3)])
fig.update_layout(title_text='Результаты голосования')
fig.write_image("voting_results.jpg")
