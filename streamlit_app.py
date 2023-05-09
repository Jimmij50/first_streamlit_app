import streamlit
import pandas
streamlit.title("hello world")

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruit_selected = streamlit.multiselect("pick some fruits:" ,list(my_fruit_list.index),['Avocado'])
fruits_to_show=my_fruit_list.loc[fruit_selected]

streamlit.dataframe(my_fruit_list)
