# -*- coding: utf-8 -*-

import base64
import hashlib
import hmac
import re
import logging
from thumbor.url_signers import BaseUrlSigner


class UrlSigner(BaseUrlSigner):
    """Validate urls and sign them using base64 hmac-sha1
    """

    def signature(self, url):
        replaced_url = re.sub("smart\/.+\)\/", "", url)
        signer_url = base64.urlsafe_b64encode(
            hmac.new(
                self.security_key, unicode(replaced_url).encode('utf-8'), hashlib.sha1
            ).digest()
        )
        return signer_url
