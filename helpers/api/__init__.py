from flask_restful import Api
# Usuarios
from resources.UsuariosResources import UsuariosResources, UsuarioResources, UsuarioLoginResources
# Posts
from resources.PostsResources import PostsResources, PostResources, PostUsuarioResources
# Likes
from resources.LikesResources import LikesResources, LikeResources
# Deslikes
from resources.DeslikesResources import DeslikesResources, DeslikeResources
# Comentarios
from resources.ComentariosResources import ComentariosResources, ComentarioResources
# Imagens
from resources.Images import ImageResource
api = Api()

# Usuarios
api.add_resource(UsuariosResources,'/usuarios')
api.add_resource(UsuarioResources,'/usuario/<int:id>')
api.add_resource(UsuarioLoginResources,'/usuario/login')

# Posts
api.add_resource(PostsResources,'/posts')
api.add_resource(PostResources,'/posts/<int:post_id>')
api.add_resource(PostUsuarioResources,'/posts/usuario/<int:id>')

# Likes
api.add_resource(LikesResources,'/likes')
api.add_resource(LikeResources,'/likes/<int:post_id>')

# Deslikes
api.add_resource(DeslikesResources,'/deslikes')
api.add_resource(DeslikeResources,'/deslikes/<int:post_id>')

# Comentarios
api.add_resource(ComentariosResources,'/comentarios')
api.add_resource(ComentarioResources,'/comentarios/<int:id>')

# Imagens
api.add_resource(ImageResource,'/images/<path:filename>')
