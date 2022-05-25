from django.shortcuts import render
from . import helpers as hlp


# Create your views here.
def home(request):
    return render(request, 'initiatives/initiatives_home.html',
                  {'title': 'Greenstock Project Hub',
                   'subheading': 'Your one stop shop for GS Project Monitoring.',
                  })

def channel_strategy(request):
    return render(request, 'initiatives/channel_strategy.html',
                  {'title': 'Channel Strategy',
                   'subheading': 'Channel Strategy page',
                  })

def demand_forecasting(request):
    return render(request, 'initiatives/demand_forecasting.html',
                  {'title': 'Demand Forecasting',
                   'subheading': 'Demand Forecasting page',
                  })

def livestock_sourcing(request):
    return render(request, 'initiatives/livestock_sourcing.html',
                  {'title': 'Livestock Sourcing',
                   'subheading': 'Livestock Sourcing page',
                  })

def supplementary_sourcing(request):
    return render(request, 'initiatives/supplementary_sourcing.html',
                  {'title': 'Supplementary Sourcing',
                   'subheading': 'Supplementary Sourcing page',
                  })

def primary_processing(request):
    client = hlp.connectBQ()
    df = (client.query(f'SELECT * FROM `gcp-wow-pvc-grnstck-prod.project_site.cost_per_kg`').to_dataframe())
    # for i,r in df.iterrows():
    #     print(r)
    return render(request, 'initiatives/primary_processing.html',
                  {'title': 'Primary Processing',
                   'subheading': 'Primary Processing page',
                   'df_cost_per_kg': df
                  })

def inv_and_prod(request):
    return render(request, 'initiatives/inv_and_prod.html',
                  {'title': 'Inventory & Production',
                   'subheading': 'Inventory & Production page',
                  })

def secondary_processing(request):
    return render(request, 'initiatives/secondary_processing.html',
                  {'title': 'Secondary Processing',
                   'subheading': 'Secondary Processing page',
                  })

def retail_and_b2b_sales(request):
    return render(request, 'initiatives/retail_and_b2b_sales.html',
                  {'title': 'Retail & B2B Sales',
                   'subheading': 'Retail & B2B Sales page',
                  })