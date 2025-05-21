import Fluent
import Vapor

struct ProductController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let products = routes.grouped("products")
        products.get(use: index)
        products.post("create", use: createPost)
        products.get(":productID", use: show)
        products.put(":productID", "edit", use: update)
        products.delete(":productID", use: delete)
    }

    // GET /products
    func index(req: Request) throws -> EventLoopFuture<[Product]> {
        return Product.query(on: req.db).all()
    }

    // POST /products/create
    func createPost(req: Request) throws -> EventLoopFuture<Product> {
        let product = try req.content.decode(Product.self)
        return product.save(on: req.db).map { product }
    }

    // GET /products/:id
    func show(req: Request) throws -> EventLoopFuture<Product> {
        return Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound))
    }

    // POST /products/:id/edit
    func update(req: Request) throws -> EventLoopFuture<Product> {
    let updatedProduct = try req.content.decode(Product.self)

    guard let idString = req.parameters.get("productID"),
          let uuid = UUID(uuidString: idString) else {
        throw Abort(.badRequest, reason: "Invalid or missing productID")
    }

    return Product.find(uuid, on: req.db)
        .unwrap(or: Abort(.notFound))
        .flatMap { product in
            product.name = updatedProduct.name
            product.price = updatedProduct.price
            product.description = updatedProduct.description
            return product.save(on: req.db).map { product }
        }
    }

    // DELETE /products/:id/delete
    func delete(req: Request) throws -> EventLoopFuture<HTTPStatus> {
        return Product.find(req.parameters.get("productID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { product in
                return product.delete(on: req.db).transform(to: .ok)
            }
    }
}
