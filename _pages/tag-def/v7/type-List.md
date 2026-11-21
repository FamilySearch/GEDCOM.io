---
title: Incomplete URI
permalink: /terms/v7/type-List.html
layout: none
redirect-from:
  - /terms/v7/type-List
...

```
error: this URI is incomplete without a fragment identifier
```

<script>
const allowed_fragments = {'Enum': '/terms/v7/type-List-Enum', 'Text': '/terms/v7/type-List-Text'};
const maybe_redirect = (event) => {
    const fragment = location.hash.substr(1)
    if (fragment in allowed_fragments && location.pathname != allowed_fragments[fragment])
        location = allowed_fragments[fragment];
};
window.addEventListener('load', maybe_redirect);
window.addEventListener('hashchange', maybe_redirect);
</script>
