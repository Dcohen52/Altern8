function colorTextareaWord(textareaId, word, color) {
    const textarea = document.getElementById(textareaId);
    const regex = new RegExp(word, 'gi');
    const matches = textarea.value.match(regex);
    if (matches) {
      const highlightedText = textarea.value.replace(regex, `<span style="color: ${color}">${word}</span>`);
      textarea.innerHTML = highlightedText;
    }
  }

colorTextareaWord('input-1', 'define', 'orange');
colorTextareaWord('input-1', 'for', 'orange');
colorTextareaWord('input-1', 'if', 'orange');
colorTextareaWord('input-1', 'then', 'orange');
colorTextareaWord('input-1', 'end', 'orange');
colorTextareaWord('input-1', 'var', 'teal');
colorTextareaWord('input-1', 'print', 'purple');