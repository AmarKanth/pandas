"""
Attributes
1. values return numpy array.
"""
import pandas as pd
adjectives = pd.Series(["Smart", "Handsome", "Charming", "Brilliant", "Humble"])
print(adjectives.size)
print(adjectives.is_unique)
print(adjectives.values)
print(adjectives.index)
print(adjectives.hasnans)
print(adjectives.dtype)

"""
sort_values
1. squeeze converts dataframe to series object.
"""
import pandas as pd
res = pd.read_csv("data/pokemon.csv", usecols=["Pokemon"]).squeeze("columns")
print(res.sort_values(ascending=True).head())
print(res.sort_values(ascending=False).head())

"""
sort_index
"""
import pandas as pd
res = pd.read_csv("data/pokemon.csv", index_col="Pokemon").squeeze("columns")
print(res.sort_index(ascending=False))

"""
get method on pandas series
1. if anyone of the value in the list not present, get method returns default value.
"""
import pandas as pd
res = pd.read_csv("data/pokemon.csv", index_col=["Pokemon"]).squeeze("columns")
print(res.get(0))
print(res.get("Bulbasaur"))
print(res.get([5, 10]))
print(res.get("Digimon", "Nonexistent"))
print(res.get(["Moltres", "Digimon"], None))

"""
Over write pandas series value
"""
import pandas as pd
res = pd.read_csv("data/pokemon.csv", usecols=["Pokemon"]).squeeze("columns")
res[0] = "Amar"
res[1500] = "Kanth"
res[[1,2,3]] = ["Firemon", "Flamemon", "Blazemon"]
print(res.head())

"""
copy method
copy will not change the original object.
"""
import pandas as pd
pokemon_df = pd.read_csv("data/pokemon.csv", usecols=["Pokemon"])
pokemon_series = pokemon_df.squeeze("columns").copy()
pokemon_series[0] = "Amar"
print(pokemon_series.head(1))
print(pokemon_df.head(1))

"""
In place parameter
1. it mutates the result set
2. it return error without copy
"""
import pandas as pd

google = pd.read_csv("data/google_stock_price.csv", usecols=["Stock Price"]).squeeze("columns").copy()

google = google.sort_values()
google.sort_values(inplace = True)
print(google)

"""
Math Methods
"""
import pandas as pd

google = pd.read_csv("data/google_stock_price.csv", usecols=["Stock Price"]).squeeze("columns")

print(google.count())
print(google.sum())
print(google.mean())
print(google.product())
print(google.std())
print(google.min())
print(google.max())
print(google.median())
print(google.mode())
print(google.describe())

"""
Broadcasting
"""
import pandas as pd

google = pd.read_csv("data/google_stock_price.csv", usecols=["Stock Price"]).squeeze("columns")

print(google + 10)
print(google - 30)
print(google * 100)
print(google.add(10))

"""
value_counts method
"""
import pandas as pd

pokemon = pd.read_csv("data/pokemon.csv", index_col= "Pokemon").squeeze("columns")

print(pokemon.value_counts())
print(pokemon.value_counts(ascending = True).head())
print(pokemon.value_counts(sort = False))
print(pokemon.value_counts(normalize = True))

"""
apply method
"""
import pandas as pd

pokemon = pd.read_csv("data/pokemon.csv", index_col= "Pokemon").squeeze("columns")

def rank_pokemon(pokemon_type):
    if pokemon_type in ["Grass", "Fire", "Water"]:
        return "Classic"
    elif pokemon_type == "Normal":
        return "Boring"
    else:
        return "TBD"

print(pokemon.apply(len))
print(pokemon.apply(rank_pokemon))