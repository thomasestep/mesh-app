import dash
import dash_core_components as dcc
import dash_html_components as html
import networkx as nx
import plotly.graph_objects as go

from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

g = nx.Graph()

nodes = [
    (0.00, 0.00), (1.00, 0.00), (2.00, 0.00),
    (0.00, 1.00), (1.00, 1.00), (2.00, 1.00),
    (0.00, 2.00), (1.00, 2.00), (2.00, 2.00)
]

for i, n in enumerate(nodes):
    g.add_node(i+1)
    g.node[i+1]['XY'] = n

#1
g.add_edge(1, 5)
g.add_edge(5, 4)
g.add_edge(4, 1)
#2
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(5, 1)
#3
g.add_edge(2, 6)
g.add_edge(6, 5)
g.add_edge(5, 2)
#4
g.add_edge(2, 3)
g.add_edge(3, 6)
g.add_edge(6, 2)
#5
g.add_edge(4, 8)
g.add_edge(8, 7)
g.add_edge(7, 4)
#6
g.add_edge(4, 5)
g.add_edge(5, 8)
g.add_edge(8, 4)
#7
g.add_edge(5, 9)
g.add_edge(9, 8)
g.add_edge(8, 5)
#8
g.add_edge(5, 6)
g.add_edge(6, 9)
g.add_edge(9, 5)

edge_trace = go.Scatter(x=[], y=[], line={'width': 0.5, 'color': '#888'}, hoverinfo='none', mode='lines')


for edge in g.edges():
    x0, y0 = g.node[edge[0]]['XY']
    x1, y1 = g.node[edge[1]]['XY']
    edge_trace['x'] += tuple([x0, x1, None])
    edge_trace['y'] += tuple([y0, y1, None])

node_trace = go.Scatter(x=[], y=[], text=[], mode='markers', hoverinfo='text')

for node in g.nodes():
    x, y = g.node[node]['XY']
    node_trace['x'] += tuple([x])
    node_trace['y'] += tuple([y])


figure = {"data": [edge_trace, node_trace],
          "layout": go.Layout(title="title", showlegend=False, hovermode='closest',
                              xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                              yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                              )}


app.layout = html.Div(children=[
    html.H1(children='Mesh'),

    dcc.Graph(
        id='mesh-graph',
        figure=figure
    )
])




if __name__ == '__main__':
    app.run_server(debug=False)
