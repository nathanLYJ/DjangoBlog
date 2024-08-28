document.addEventListener('DOMContentLoaded', function() {
    const tagInput = document.getElementById('tag-input');
    const addTagButton = document.getElementById('add-tag');
    const tagList = document.getElementById('tag-list');
    const tagsField = document.querySelector('input[name="tags"]');

    function addTag() {
        const tagName = tagInput.value.trim();
        if (tagName) {
            const tagSpan = document.createElement('span');
            tagSpan.className = 'bg-blue-100 text-blue-800 text-sm font-semibold mr-2 mb-2 px-2.5 py-0.5 rounded';
            tagSpan.innerHTML = `#${tagName} <button type="button" class="ml-1 text-blue-600 hover:text-blue-800" onclick="removeTag(this)">×</button>`;
            tagList.appendChild(tagSpan);
            tagInput.value = '';
            updateTagsField();
        }
    }

    tagInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            addTag();
        }
    });

    addTagButton.addEventListener('click', addTag);

    window.removeTag = function(button) {
        button.parentElement.remove();
        updateTagsField();
    }

    function updateTagsField() {
        const tags = Array.from(tagList.children).map(span => span.textContent.trim().slice(1, -1));
        tagsField.value = tags.join(',');
    }

    // 초기 태그 필드 업데이트
    updateTagsField();
});

// CSRF 토큰 처리 (필요한 경우)
function getCsrfToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}