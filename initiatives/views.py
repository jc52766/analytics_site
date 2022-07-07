from ssl import ALERT_DESCRIPTION_UNRECOGNIZED_NAME
from django.shortcuts import render
from . import helpers as hlp
import pandas as pd

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
    storage_client = hlp.connectStorage()

    # get cost per kg data
    df_cost_per_kg = pd.read_json(hlp.get_file_from_bucket(client=storage_client, bucket='gs_website', fn='data/cost_per_kg.json').download_as_string(), lines=True) 
    
    # add formatted columns for display purposes
    for col in ['Tamworth', 'Naracoorte', 'Total_East_Coast', 'ACC', 'VV_Walsh', 'Total_West_Coast']:
        df_cost_per_kg[col+'_formatted'] = list(map(lambda x: "${:,.2f}".format(x), df_cost_per_kg[col]))
    
    # get cost per kg data
    df_heads = pd.read_json(hlp.get_file_from_bucket(client=storage_client, bucket='gs_website', fn='data/heads.json').download_as_string(), lines=True) 
    
    # add formatted columns for display purposes
    for col in ['Tamworth', 'Naracoorte', 'Total_East_Coast', 'ACC', 'VV_Walsh', 'Total_West_Coast']:
        df_heads[col+'_formatted'] = list(map(lambda x: "{:,}".format(x), df_heads[col]))
    
    return render(request, 'initiatives/primary_processing.html',
                  {'title': 'Primary Processing',
                   'subheading': 'Primary Processing page',
                   'df_cost_per_kg': df_cost_per_kg,
                   'df_heads': df_heads,
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

def demand_as_cattle(request):
    storage_client = hlp.connectStorage()
    # get cost per kg data
    df_demand_as_cattle = pd.read_json(hlp.get_file_from_bucket(client=storage_client, bucket='gs_website', fn='data/demand_as_cattle_summary.json').download_as_string(), lines=False).fillna(0).sort_values(by=["heads"], ascending=False).reset_index()
    df_demand_as_cattle = df_demand_as_cattle.query("heads > 0")
    
    values_to_remove = ['trim','fat'] #['trim','fat','tomahawk','ribs prepared','bone','shank hq']
    pattern = '|'.join(values_to_remove)
    df_demand_as_cattle = df_demand_as_cattle.loc[~df_demand_as_cattle['primal_group'].str.contains(pattern, case=False, regex=True)].reset_index()
    
    df_demand_as_cattle.heads = df_demand_as_cattle.heads.round()
    
    # wide data for line chart
    #wide_dat = df_demand_as_cattle.pivot(index='fiscalWeekStartDate',columns='primal_group',values='heads').reset_index().fillna(0)
    wide_dat = df_demand_as_cattle.pivot(index=['fiscalWeekStartDate','master_cattle_type','crm_site'],columns='primal_group',values='heads').reset_index().fillna(0)
    
    return render(request, 'initiatives/demand_as_cattle.html',
                    {#'title': 'Demand As Cattle',
                    'df_demand_as_cattle' : df_demand_as_cattle,
                    'json_demand_as_cattle' : df_demand_as_cattle.drop(columns='index').to_json(orient='records'),
                    'json_demand_as_cattle_wide' : wide_dat.to_json(orient='records'),
                    'distinct_dates' : df_demand_as_cattle.fiscalWeekStartDate.sort_values().unique(),
                    'max_date' : df_demand_as_cattle.fiscalWeekStartDate.max(),
                    'min_date' : df_demand_as_cattle.fiscalWeekStartDate.min(),
                    'distinct_cattle_type' : df_demand_as_cattle.master_cattle_type.sort_values().unique(),
                    'distinct_crm_site' : df_demand_as_cattle.crm_site.sort_values().unique(),
                    })

def yield_trees(request):
    storage_client = hlp.connectStorage()
    # get cost per kg data
    df_yield_tree = pd.read_json(hlp.get_file_from_bucket(client=storage_client, bucket='gs_website', fn='data/yield_tree.json').download_as_string(), lines=False)
    
    return render(request, 'initiatives/yield_trees.html',
                    {'title': 'Yield Trees',
                    'json_yield_tree' : df_yield_tree.to_json(orient='split'),
                    })
