import pandas as pd
from bokeh.plotting import figure
from bokeh.models import Range1d,LinearAxis,ColumnDataSource,HoverTool


def Pareto(DATA_FRAME,column_index,column_values,color="#9B59B6"):
    
    #Do pareto table.
    TOTAL=DATA_FRAME[column_values].sum()
    DATA_FRAME['Porcentaje']=100*(DATA_FRAME[column_values]/TOTAL)
    DATA_FRAME['Porcentaje_acumulado']=DATA_FRAME['Porcentaje'].cumsum()
    
    #Set pareto table how the source of next graphs.
    DataSourse=ColumnDataSource(DATA_FRAME)
    
    #Create the figure called figure 1
    figure1=figure(
        x_range=DATA_FRAME[column_index],title=column_values,
        plot_width=600,plot_height=450,
        tools='reset,box_zoom',toolbar_location='below'
        )
    
    #General sets, how label´s name, color´s grid etc.
    figure1.xgrid.grid_line_color=None
    figure1.xaxis.axis_label=column_index
    figure1.xaxis.major_label_text_font_size='15px'
    figure1.yaxis.axis_label="$"+column_values
    figure1.xgrid.grid_line_color=None
    figure1.ygrid.grid_line_alpha=0.7
    figure1.toolbar.autohide=True
    figure1.y_range.start = 0
    figure1.x_range.range_padding = 0.1
    figure1.xaxis.major_label_orientation = 1
    figure1.xgrid.grid_line_color = None
    
    # Create the seconde y axis for the % acumulate
    figure1.extra_y_ranges = {"y2": Range1d(start = 0, end = 110)}
    figure1.add_layout(LinearAxis(y_range_name = "y2"), 'right')
    
    #Create the Graphs
    figure1.vbar(
        x=column_index,top=column_values,
        width=0.9,fill_color=color,
        line_color="#2E4053",source=DataSourse
        )
    figure1.line(
        x=column_index,y='Porcentaje_acumulado',
        y_range_name='y2',source=DataSourse
        )
    figure1.scatter(
        x=column_index,y='Porcentaje_acumulado',
        y_range_name='y2',source=DataSourse)
    
    #Create the hover for can show the values of graph
    hover=HoverTool(
        tooltips=[
            (column_index,'@'+column_values),
            ('% profit acumulete','@Porcentaje_acumulado'), 
            ('% profit','@Porcentaje')]
            )
    figure1.add_tools(hover)
    return figure1


def barra_stackeada(DATA_FRAME,column_index,column_columns,column_values):
    PRODUCTS=DATA_FRAME.groupby([column_index,column_columns])[column_values].sum()
    PRODUCTS_U=PRODUCTS.unstack(level=1,fill_value=0)
    PRODUCTS_U=PRODUCTS_U.reset_index()
    PRODUCTS_TOTAL=DATA_FRAME.groupby([column_index])[column_values].sum().reset_index()
    # UNION DE TABLAS
    TABLA_TOTAL=pd.merge(PRODUCTS_U,PRODUCTS_TOTAL)
    TABLA_TOTAL_SORT=TABLA_TOTAL.sort_values(by=column_values,ascending=False)
    sellers=list(TABLA_TOTAL_SORT[column_index])
    columns=list(TABLA_TOTAL_SORT.columns)
    figure1=figure(
        x_range=sellers,height=250,title=column_values,
        plot_width=1200,plot_height=800,
        tools='reset,box_zoom',toolbar_location='below',
        tooltips="$name @"+column_index+":@$name"
        )
    figure1.xgrid.grid_line_color=None

    figure1.xaxis.axis_label=column_index
    figure1.yaxis.axis_label='$'+column_values
    figure1.xaxis.major_label_text_font_size='15px'
    figure1.xgrid.grid_line_color=None
    figure1.ygrid.grid_line_alpha=0.7
    figure1.yaxis.major_label_text_font_size='15px'

    figure1.toolbar.autohide=True
    figure1.y_range.start = 0
    figure1.x_range.range_padding = 0.1
    figure1.xaxis.major_label_orientation = 1
    figure1.xgrid.grid_line_color = None
    figure1.vbar_stack(
        columns[1:-1],x=column_index, width=0.9,
        color=[
            '#922B21','#B03A2E','#76448A','#6C3483',
            '#1F618D','#2874A6','#117864','#0B5345',
            '#196F3D','#7D6608','#6E2C00','#F5CBA7',
            '#85C1E9'
            ],
        line_color="#17202A", 
        source=TABLA_TOTAL_SORT,legend_label=columns[1:-1])
    return figure1
