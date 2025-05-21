// swift-tools-version: 6.1
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "projektowanie_obiektowe",
    dependencies: [
        .package(url: "https://github.com/vapor/vapor.git", from: "4.80.0"),
        .package(url: "https://github.com/vapor/fluent.git", from: "4.8.0"),
        .package(url: "https://github.com/vapor/fluent-sqlite-driver.git", from: "4.0.0"),
    ],
    targets: [
        // Targets are the basic building blocks of a package, defining a module or a test suite.
        // Targets can depend on other targets in this package and products from dependencies.
        .executableTarget(
            name: "projektowanie_obiektowe",
            dependencies: [
                .product(name: "Vapor", package: "vapor"),
                .product(name: "Fluent", package: "fluent"),
                .product(name: "FluentSQLiteDriver", package: "fluent-sqlite-driver"),
            ],
            path: "Sources",
            sources: ["main.swift", "routes.swift", "controllers", "models", "migrations"],
            swiftSettings: [
                .unsafeFlags(["-parse-as-library"], .when(configuration: .debug))
            ]
        )
    ],
)
