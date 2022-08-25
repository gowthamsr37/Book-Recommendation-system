mkdir -p ~/.streamlit/

echo "\
[theme]\n\
primaryColor = '#E694FF'\n\
backgroundColor = '#00172B'\n\
secondaryBackgroundColor = '#0083B8'\n\
textColor = '#FFF'\n\
font = 'sans serif'\n\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml