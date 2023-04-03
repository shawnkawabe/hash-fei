import pandas as pd
import dataframe_image as dfi
# import numpy as np

dict = {'Name' : ['Martha', 'Tim', 'Rob', 'Georgia'],
        'Maths' : [87, 91, 97, 95],
        'Science' : [83, 99, 84, 76]}
df = pd.DataFrame(dict)
print(df)

df_styled = df.style.background_gradient() #adding a gradient based on values in cell

dfi.export(df_styled,"mytable.png")