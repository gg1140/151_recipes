export abstract class ResourceData {
  dataType: string;
  id: string;
  name: string;

  constructor(objectModel: {}) {
    this.name = objectModel["name"];
    this.id = objectModel["id"];
  }
}
