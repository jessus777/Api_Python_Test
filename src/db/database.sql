	-- Parte 1: Crear la base de datos si no existe
	IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'test_database')
	BEGIN
		CREATE DATABASE test_database;
	END
	GO

	-- Parte 2: Usar la base de datos
	USE test_database;
	GO

	-- Verificar si la tabla ya existe y eliminarla si es necesario
	IF OBJECT_ID('dbo.solicitud', 'U') IS NOT NULL
	DROP TABLE dbo.solicitud;
	GO

	-- Verificar si la tabla ya existe y eliminarla si es necesario
	IF OBJECT_ID('dbo.grimoires', 'U') IS NOT NULL
	DROP TABLE dbo.grimoires;
	GO

	-- Crear la tabla grimoires
	CREATE TABLE dbo.grimoires (
		id UNIQUEIDENTIFIER NOT NULL DEFAULT NEWID(),   -- Llave primaria
		nombre VARCHAR(50) NOT NULL,                      -- Nombre del grimorio
		nivel INT NOT NULL,                             -- Nivel del grimorio
		PRIMARY KEY (id)                                -- Definir la clave primaria
	);
	GO

	-- Insertar datos en la tabla grimoires
	INSERT INTO dbo.grimoires (id, nombre, nivel)
	VALUES 
		('7489729E-9FBD-4627-A850-D3DD447C7E8A', 'Book of Shadows', 1),
		('12345678-1234-1234-1234-1234567890AB', 'Tome of Ancient Wisdom', 2),
		('87654321-4321-4321-4321-0987654321BA', 'Codex of the Arcane', 3),
		('11223344-5566-7788-99AA-BBCCDDEEFF00', 'Necronomicon', 4),
		('AABBCCDD-EEFF-1122-3344-556677889900', 'Book of Lost Spells', 5),
		('99887766-5544-3322-1100-AABBCCDDEEFF', 'Grimoire of Enchantments', 6);
	GO

	-- Crear la tabla solicitud con la clave foránea configurada para eliminar en cascada
	CREATE TABLE dbo.solicitud (
		id INT IDENTITY(1,1) PRIMARY KEY,                  -- Llave primaria autoincrementable
		nombre VARCHAR(20) NOT NULL,                       -- Nombre (varchar de 20 caracteres)
		apellido VARCHAR(20) NOT NULL,                     -- Apellido (varchar de 20 caracteres)
		identificacion VARCHAR(20) NOT NULL,               -- Identificación (varchar de 20 caracteres)
		edad INT CHECK (edad >= 10 AND edad <= 99),        -- Edad (entero de 2 dígitos)
		afinidad_magica VARCHAR(20) NOT NULL,              -- Afinidad mágica (varchar)
		estatus VARCHAR(20) NOT NULL,              -- estatus de la solicitud (varchar)
		grimoire_id UNIQUEIDENTIFIER NOT NULL,             -- ID del grimorio relacionado
		FOREIGN KEY (grimoire_id) REFERENCES dbo.grimoires(id) ON DELETE CASCADE  -- Clave foránea con eliminación en cascada
	);
	GO
