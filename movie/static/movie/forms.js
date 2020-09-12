function jumpToPage(max_page) {
    let page = document.getElementById('jump').value;
    if (page !== undefined) {
        page = parseInt(page, 10)
        if (!isNaN(page) && page > 0 && page <= max_page) {
            window.location.href = "?page=" + page;
        }
    }
}

function search(base_url) {
    let selector = document.getElementById('searchCategory');
    let category = selector.options[selector.selectedIndex].value;
    let query = document.getElementById('queryInput').value;
    if (query !== undefined && query !== '') {
        window.location.href = '/search/' + category + '/' + query;
    }
}