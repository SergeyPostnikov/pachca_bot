import plotly.graph_objects as go


def vote():
    options = ['Опция 1', 'Опция 2']
    votes = [150, 50]
    fig = go.Figure(data=[go.Bar(x=options, y=votes)])
    fig.update_layout(
        title_text='Результаты голосования', 
        xaxis_title='Опции', 
        yaxis_title='Количество голосов'
    )
    fig.write_image("voting_results_bar.jpg")
