{
"total_cost": {
    "type" : "custom.googleapis.com/total_cost",
    "labels" : [],
    "metricKind" : "CUMULATIVE",
    "valueType" : "MONEY",
    "unit" : "dollars",
    "description" : "Total cost from queries across all jobs",
    "displayName" : "Total Cost per day"
},
"total_number_of_queries": {
    "type" : "custom.googleapis.com/total_number_of_queries",
    "labels" : [],
    "metricKind" : "CUMULATIVE",
    "valueType" : "INT64",
    "unit" : "queries",
    "description" : "The total number of queries across all jobs",
    "displayName" : "Total number of queries"
},
"total_number_of_rows_processed": {
    "type" : "custom.googleapis.com/total_number_rows_processed",
    "labels" : [],
    "metricKind" : "CUMULATIVE",
    "valueType" : "INT64",
    "unit" : "rows",
    "description" : "The total number of rows processed across all jobs",
    "displayName" : "Total number of rows processed"
},
"total_size_of_data": {
    "type" : "custom.googleapis.com/total_size_of_data",
    "labels" :[],
    "metricKind" : "CUMULATIVE",
    "valueType" : "DOUBLE",
    "unit" : "GBy",
    "description" : "The total amount of data processed across all jobs",
    "displayName" : "Total size of processed data across all jobs"
},
"total_time_required_for_queries": {
    "type" : "custom.googleapis.com/total_time_required_for_queries",
    "labels" : [],
    "metricKind" : "CUMULATIVE",
    "valueType" : "DOUBLE",
    "unit" : "s",
    "description" : "The total amount of time required to run all queries across all jobs",
    "displayName" : "Total time required to run all queries across all jobs"
},
"table_loader_total_load_duration": {
    "type": "custom.googleapis.com/table_loader_total_load_duration",
    "labels": [],
    "metricKind": "CUMULATIVE",
    "valueType": "INT64",
    "unit": "s",
    "description": "The aggregate time spent on loading data onto big query by the script table_loader.py",
    "displayName": "Table loader: total load duration"
},
"table_loader_total_gigabytes_pulled_by_script": {
    "type": "custom.googleapis.com/table_loader_total_gigabytes_pulled_by_script",
    "labels": [],
    "metricKind": "CUMULATIVE",
    "valueType": "INT64",
    "unit": "GBy",
    "description": "The aggregate number of Gigabytes pulled from Home Depot sources by the script table_loader.py",
    "displayName": "Table loader: total Gigabytes pulled from Home Depot sources"
},
"table_loader_total_rows_placed_into_bq": {
    "type": "custom.googleapis.com/table_loader_total_rows_placed_into_bq",
    "labels": [],
    "metricKind": "CUMULATIVE",
    "valueType": "INT64",
    "unit": "rows",
    "description": "The aggregate number of rows placed into Big Query by the script table_loader.py",
    "displayName": "Table loader: total rows placed into Big Query"
},
"table_loader_total_gigabytes_placed_into_bq": {
    "type": "custom.googleapis.com/table_loader_total_gigabytes_placed_into_bq",
    "labels": [],
    "metricKind": "CUMULATIVE",
    "valueType": "INT64",
    "unit": "GBy",
    "description": "The aggregate number of Gigabytes placed into Big Query by the script table_loader.py",
    "displayName": "Table loader: total Gigabytes placed into Big Query"
},
"delta_loader_total_duration": {
    "type": "custom.googleapis.com/delta_loader_total_duration",
    "labels": [],
    "metricKind": "CUMULATIVE",
    "valueType": "INT64",
    "unit": "s",
    "description": "The aggregate time spent generating the delta or change in datasets by the script delta loader",
    "displayName": "Delta loader: total computational time"
},
"delta_loader_total_rows_processed": {
    "type": "custom.googleapis.com/delta_loader_total_rows_processed",
    "labels": [],
    "metricKind": "CUMULATIVE",
    "valueType": "INT64",
    "unit": "rows",
    "description": "The aggregate number of rows processed in generating the delta or change in datasets by the script delta loader",
    "displayName": "Delta loader: total rows processed"
},
"delta_loader_size_of_delta": {
    "type": "custom.googleapis.com/delta_loader_size_of_delta",
    "labels": [],
    "metricKind": "GAUGE",
    "valueType": "INT64",
    "unit": "rows",
    "description": "The size in rows of the generated delta or change in datasets by the script delta loader",
    "displayName": "Delta loader: size of delta"
}
}
