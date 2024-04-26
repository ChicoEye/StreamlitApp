import streamlit as st

def main():
    st.title('Basic Streamlit App')
    st.write('Welcome to my first Streamlit app!')

    # Add some widgets
    user_input = st.text_input('Enter your name:', 'John Doe')
    button_clicked = st.button('Click me!')

    # Display output based on user interaction
    if button_clicked:
        st.write(f'Hello, {user_input}!')

if __name__ == "__main__":
    main()
