    bins = [0, 500, 1000, 2500, 5000, 10000, 20000, 30000]
    labels = [
        "0-500",
        "501-1000",
        "1001-2500",
        "2501-5000",
        "5001-10000",
        "10000-20000",
        "20000-30000",
    ]
    df["color_category"] = pd.cut(
        df["primary_energy_consumption"], bins=bins, labels=labels, right=False
    )

    # Define a custom color scale with green as a transitionary color
    color_map = {
        "0-500": "yellow",
        "501-1000": "light green",  # Transitioning towards green
        "1001-2500": "green",  # Midpoint green
        "2501-5000": "sky blue",  # Transitioning away from green towards blue
        "5001-10000": "#0b2c4d",  # Dark blue
        "10000-20000": "#0b2c4d",  # Dark blue
        "5001-10000": "#0b2c4d",  # Dark blue
        "10000-20000": "orange",
        "20000-30000": "red",
    }

    fig = px.choropleth(
        df,
        locations="iso_code",
        animation_frame="year",
        color="color_category",  #
        range_color=[],
        color_discrete_map=color_map,
        hover_name="country",  # column to add to hover information
        projection="natural earth",
    )

    