# Templates in Django

## Templates

Templates allow a website to be modular and easily extendable. With templates the html and css code is nicely separated from the core (main) logic.

For rendering the templates the [`render()`](https://docs.djangoproject.com/en/3.2/topics/http/shortcuts/#render) shortcut function. Code is injected in the html templates using the special syntax of using `{{ PROPERTY }}`. 

Example:

```python

context = {
    "text" : "some fancy text"
}

render(request, "file.html", context)
```

```html
<div>
{{ text }}
</div>
```

A commonly used method of separating repeated content is using the [`include`](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#include) directive inside a template. This is useful when common UI components are shown in multiple pages - navigation pane, sidebar, footer, etc.

Example:

```html
{% include other.html %}

...
```


For detailed step-by-step instructions follow the second part of: [Django Getting Started Guide Part 3](https://docs.djangoproject.com/en/3.2/intro/tutorial03/)

## Miscellaneous 

- 10 finger typing - A good suggestion for online typing lessons is: https://www.typingstudy.com . Try to learn to type accurately. Speed will come over time naturally.

note: configure the keyboard from the lower left section of the site.