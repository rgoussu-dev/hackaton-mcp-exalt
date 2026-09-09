import org.jetbrains.kotlin.gradle.dsl.JvmTarget

plugins {
    kotlin("jvm") version "2.4.20"
    application
}

repositories {
    mavenCentral()
}

// Kotlin 2.4.20 cannot emit a JVM 27 target yet; keep both compilers aligned on 26.
kotlin {
    compilerOptions {
        jvmTarget = JvmTarget.JVM_26
    }
}

java {
    sourceCompatibility = JavaVersion.toVersion(26)
    targetCompatibility = JavaVersion.toVersion(26)
}

application {
    mainClass.set("MainKt")
}
