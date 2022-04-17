create table if not exists Usuario(
	id serial primary key,
	nome varchar(255) not null unique,
	senha varchar(30) not null,
	idade integer
);

create table if not exists Agenda(
	id serial primary key,
	foreign key(id) references usuario(id)
);

create table if not exists CronogramaDeMaterias(
	id serial primary key,
	materia varchar(20),
	descricao varchar(255),
	data timestamp,
	foreign key(id) references agenda(id),
	foreign key(id) references usuario(id)
);

create table if not exists Materias(
	id serial primary key,
	materia varchar(20),
	area varchar(20),
	foreign key(id) references cronogramadematerias(id)
);

create table if not exists Lembretes(
	id serial primary key,
	nome varchar(255),
	descricao varchar(255),
	data timestamp,
	agenda_id integer,
	usuario_id integer,
  FOREIGN KEY(agenda_id) REFERENCES Agenda(id),
  FOREIGN KEY(usuario_id) REFERENCES Usuario(id)
);


create table if not exists Metas(
	id serial primary key,
	nome varchar(255),
	descricao varchar(255),
	status float,
	prazo timestamp,
	foreign key(id) references agenda(id),
	foreign key(id) references usuario(id)
);

create table if not exists LinksUteis(
	id serial primary key,
	titulo varchar(50),
	link varchar(255),
	foreign key(id) references usuario(id)
);
