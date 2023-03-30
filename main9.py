import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('stream 入門1')

st.write('Display Image')
img = Image.open('sample.png')
st.image(img, caption='picture', use_column_width=True)


st.write('DataFrame1')

df = pd.DataFrame({
 '1列目': [1,2,3,4] ,
 '2列目': [10,20,40,30]  
})
#st.write(df)

#st.dataframe(df.style.highlight_max(axis=0),width=500, height=500)

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df2 = pd.DataFrame(
	np.random.rand(20,3),
	columns=[ 'a', 'b', 'c']   
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)


df = pd.DataFrame(
	np.random.rand(100,2)/[50,50] + [35.69, 139.70],
	columns=[ 'lat', 'lon']   
)
st.map(df)