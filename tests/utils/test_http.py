from unittest.mock import patch

from app.utils.http import DEFAULT_TIMEOUT, get, head, post


class TestHTTPWrappers:
    """Test HTTP wrapper functions apply default timeouts."""

    @patch("app.utils.http.requests.get")
    def test_get_default_timeout(self, mock_get):
        get("https://example.com")
        mock_get.assert_called_once_with("https://example.com", timeout=DEFAULT_TIMEOUT)

    @patch("app.utils.http.requests.get")
    def test_get_custom_timeout(self, mock_get):
        get("https://example.com", timeout=30)
        mock_get.assert_called_once_with("https://example.com", timeout=30)

    @patch("app.utils.http.requests.get")
    def test_get_passes_kwargs(self, mock_get):
        get("https://example.com", stream=True, headers={"X-Test": "1"})
        mock_get.assert_called_once_with(
            "https://example.com", stream=True, headers={"X-Test": "1"}, timeout=DEFAULT_TIMEOUT
        )

    @patch("app.utils.http.requests.post")
    def test_post_default_timeout(self, mock_post):
        post("https://example.com", data={"key": "val"})
        mock_post.assert_called_once_with("https://example.com", data={"key": "val"}, timeout=DEFAULT_TIMEOUT)

    @patch("app.utils.http.requests.post")
    def test_post_tuple_timeout(self, mock_post):
        post("https://example.com", timeout=(5, 60))
        mock_post.assert_called_once_with("https://example.com", timeout=(5, 60))

    @patch("app.utils.http.requests.head")
    def test_head_default_timeout(self, mock_head):
        head("https://example.com")
        mock_head.assert_called_once_with("https://example.com", timeout=DEFAULT_TIMEOUT)
