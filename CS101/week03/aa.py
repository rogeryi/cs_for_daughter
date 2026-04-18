def print_with_pause(texts, pause_text="按回车键继续..."):
    """逐行显示文本，每行后暂停"""
    for line in texts:
        print(line)
        input(pause_text)

