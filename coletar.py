from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto('https://49s.co.uk/49s', wait_until='networkidle')
    pg.wait_for_timeout(5000)
    open('pagina.txt', 'w', encoding='utf-8').write(pg.inner_text('body'))
    b.close()
