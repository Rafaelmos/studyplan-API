create table if not exists usuario(
	id serial primary key,
	nome varchar(255) not null unique,
	senha varchar(30) not null,
	idade integer
);

create table if not exists materias(
	id serial primary key,
	materia varchar(20),
	area varchar(20),
	usuario_id integer,
	foreign key(usuario_id) references usuario(id)
);

create table if not exists agenda(
	id serial primary key,
	usuario_id integer,
	foreign key(usuario_id) references usuario(id)
);

create table if not exists cronogramadematerias(
	id serial primary key,
	descricao varchar(255),
	data timestamp,
	agenda_id integer,
	usuario_id integer,
	materia_id integer,
  	foreign key(agenda_id) references agenda(id),
  	foreign key(usuario_id) references usuario(id),
	foreign key(materia_id) references materias(id)
);

create table if not exists lembretes(
	id serial primary key,
	nome varchar(255),
	descricao varchar(255),
	data timestamp,
	agenda_id integer,
	usuario_id integer,
  foreign key(agenda_id) references agenda(id),
  foreign key(usuario_id) references usuario(id)
);


create table if not exists metas(
	id serial primary key,
	nome varchar(255),
	descricao varchar(255),
	status float,
	prazo timestamp,
	agenda_id integer,
	usuario_id integer,
  foreign key(agenda_id) references agenda(id),
  foreign key(usuario_id) references usuario(id)
);

create table if not exists linksuteis(
	id serial primary key,
	titulo varchar(50),
	link varchar(255),
	usuario_id integer,
  foreign key(usuario_id) references usuario(id)
);
