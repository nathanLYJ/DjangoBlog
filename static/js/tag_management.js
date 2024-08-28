document.addEventListener('DOMContentLoaded', function() {
    const tagInput = document.getElementById('tag-input');
    const addTagButton = document.getElementById('add-tag');
    const tagList = document.getElementById('tag-list');
    const hiddenTagsInput = document.getElementById('tags-hidden');

    function addTag(tagName) {
        if (tagName.trim() === '') return;

        const tagSpan = document.createElement('span');
        tagSpan.className = 'bg-blue-100 text-blue-800 text-sm font-semibold mr-2 mb-2 px-2.5 py-0.5 rounded';
        tagSpan.innerHTML = `
            ${tagName}
            <button type="button" class="ml-1 text-blue-600 hover:text-blue-800" onclick="removeTag(this, '${tagName}')">×</button>
        `;
        tagList.appendChild(tagSpan);
        updateHiddenInput();
        tagInput.value = '';
    }

    window.removeTag = function(button, tagName) {
        button.parentElement.remove();
        updateHiddenInput();
    };

    function updateHiddenInput() {
        const tags = Array.from(tagList.children).map(span => span.textContent.trim());
        hiddenTagsInput.value = tags.join(',');
    }

    addTagButton.addEventListener('click', () => addTag(tagInput.value));
    tagInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            addTag(this.value);
        }
    });

    // 초기 태그 설정
    updateHiddenInput();
});