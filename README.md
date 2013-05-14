# Pelican-Gist
Pelican-Gist is a plugin for [Pelican](http://blog.getpelican.com/) that makes it very easy to embed one or more Gists within an article.


## AUTHORS
* [Kevin Richardson](https://github.com/kfr2)


## LICENSE
Released under the MIT License.  See full details in the `LICENSE` file.


## INSTALLATION
Download or clone this [repository](https://github.com/kfr2/pelican-gist) to a `plugin` directory and rename it to something like `gist`. Edit `pelicanconf.py` to include the following:

    PLUGIN_PATH = 'plugins/'
    PLUGINS = ('gist', )

See the [pelican plugins README](https://github.com/getpelican/pelican-plugins/) for more information.


## USAGE
Locate the username and ID of the Gist you would like to embed. For example, in the Gist at `https://gist.github.com/kfr2/5580453`, `kfr2` is the username and `5580453` is the ID. Place the following inside an article's body:

    [[ gist username:ID ]]

When you use Pelican to build your site, the block above will be replaced with:

    <script src="https://gist.github.com/username/ID.js"></script>

Any `[[ gist ... ]]` blocks within an article will be replaced accordingly.