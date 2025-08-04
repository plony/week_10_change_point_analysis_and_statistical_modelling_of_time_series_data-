import pandas as pd

def compile_geopolitical_events():
    """
    Compiles a structured dataset of major geopolitical events.
    """
    events_data = [
        {'event_date': '1990-08-02', 'event_name': 'Iraqi Invasion of Kuwait', 'description': 'Major supply disruption.'},
        {'event_date': '2001-09-11', 'event_name': 'September 11 Attacks', 'description': 'Geopolitical uncertainty.'},
        {'event_date': '2008-07-01', 'event_name': 'Global Financial Crisis intensifies', 'description': 'Drop in global demand.'},
        {'event_date': '2014-11-27', 'event_name': 'OPEC decides not to cut production', 'description': 'Oversupply and low prices.'},
        {'event_date': '2020-03-11', 'event_name': 'COVID-19 Pandemic declared', 'description': 'Unprecedented drop in demand.'},
        {'event_date': '2022-02-24', 'event_name': 'Russian Invasion of Ukraine', 'description': 'Sanctions and supply concerns.'},
    ]
    events_df = pd.DataFrame(events_data)
    events_df['event_date'] = pd.to_datetime(events_df['event_date'])
    return events_df

if __name__ == '__main__':
    events_df = compile_geopolitical_events()
    output_path = "../data/processed/geopolitical_events.csv"
    events_df.to_csv(output_path, index=False)
    print(f"Geopolitical events saved to {output_path}")